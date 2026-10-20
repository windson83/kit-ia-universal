import importlib.util
import json
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'scripts/kit.py'
spec = importlib.util.spec_from_file_location('kit', CLI)
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)

def workspace_temp():
    # Keep generated projects beside the distribution, never inside its sealed files.
    temp = tempfile.TemporaryDirectory(prefix='kit-ia-test-', dir=ROOT.parent)
    target = Path(temp.name).resolve()
    if target.parent != ROOT.parent.resolve() or not target.name.startswith('kit-ia-test-'):
        raise ValueError('Unexpected temporary cleanup path')
    return temp

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = workspace_temp()
        self.addCleanup(self.temp.cleanup)
        self.dest = Path(self.temp.name) / 'project with spaces'

    def run_cli(self, *args, ok=True):
        result = subprocess.run([sys.executable,str(CLI),*args], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0 if ok else 1, result.stdout + result.stderr)
        return result

    def install(self, profile='codex', *extra, ok=True):
        return self.run_cli('install','--profile',profile,'--dest',str(self.dest),*extra,ok=ok)

    def test_dry_run_has_no_writes(self):
        self.install()
        self.assertFalse(self.dest.exists())

    def test_all_profiles_and_references(self):
        for profile,prefix in [('codex','.agents/skills'),('claude','.claude/skills'),('generic','ia-kit/skills')]:
            self.install(profile,'--apply')
            self.assertEqual(len(list((self.dest/prefix).glob('*/SKILL.md'))),19)
            self.assertTrue((self.dest/prefix/'arquiteto-de-software/references/adr-template.md').is_file())
        exported = json.loads((self.dest/'ia-kit/catalogo.json').read_text(encoding='utf-8'))
        self.assertEqual(len(exported['capacidades']),19)

    def test_selection_and_native_claude_agents(self):
        self.install('claude','--only','backend-dev','debugger','--agents','--apply')
        self.assertEqual(len(list((self.dest/'.claude/skills').glob('*/SKILL.md'))),2)
        text = (self.dest/'.claude/agents/backend-dev.md').read_text(encoding='utf-8')
        self.assertIn('model: inherit',text)
        self.assertIn('skills:\n  - backend-dev',text)

    def test_noop_preserves_mtime(self):
        self.install('codex','--apply')
        file = self.dest/'.agents/skills/backend-dev/SKILL.md'
        before = file.stat().st_mtime_ns
        self.install('codex','--apply')
        self.assertEqual(before,file.stat().st_mtime_ns)
        self.assertFalse((self.dest/'.ia-kit-backups').exists())

    def test_conflict_aborts_entire_plan(self):
        file = self.dest/'.agents/skills/backend-dev/SKILL.md'
        file.parent.mkdir(parents=True)
        file.write_text('user customization',encoding='utf-8')
        self.install('codex','--apply',ok=False)
        self.assertEqual(file.read_text(),'user customization')
        self.assertFalse((self.dest/'.agents/skills/product-analyst').exists())

    def test_update_backups_and_unrelated_files(self):
        file = self.dest/'.agents/skills/backend-dev/SKILL.md'
        file.parent.mkdir(parents=True)
        file.write_text('user customization',encoding='utf-8')
        unrelated = self.dest/'AGENTS.md'
        unrelated.write_text('project rules',encoding='utf-8')
        extra = file.parent/'custom.txt'
        extra.write_text('keep',encoding='utf-8')
        self.install('codex','--apply','--update')
        backups = list((self.dest/'.ia-kit-backups').glob('*/.agents/skills/backend-dev/SKILL.md'))
        self.assertEqual(len(backups),1)
        self.assertEqual(backups[0].read_text(),'user customization')
        self.assertEqual(unrelated.read_text(),'project rules')
        self.assertEqual(extra.read_text(),'keep')

    def test_unknown_and_invalid_options(self):
        self.install('codex','--only','not-a-skill','--apply',ok=False)
        self.install('codex','--agents','--apply',ok=False)
        self.assertFalse(self.dest.exists())

    def test_parent_file_collision_preflight(self):
        self.dest.mkdir(parents=True)
        (self.dest/'.agents').write_text('not a directory')
        self.install('codex','--apply',ok=False)
        self.assertEqual((self.dest/'.agents').read_text(),'not a directory')

    def test_distribution_cannot_be_install_target(self):
        self.run_cli('install','--profile','generic','--dest',str(ROOT/'export'),'--apply',ok=False)
        self.assertFalse((ROOT/'export').exists())

    def test_link_escape(self):
        outside = Path(self.temp.name)/'outside'
        outside.mkdir()
        self.dest.mkdir()
        link = self.dest/'.agents'
        try:
            link.symlink_to(outside,target_is_directory=True)
        except OSError:
            self.skipTest('Symlinks require privileges on this Windows host')
        self.install('codex','--apply',ok=False)
        self.assertFalse(list(outside.iterdir()))

    def test_rollback_after_write_failure(self):
        class Args:
            profile='codex'
            only=['backend-dev','debugger']
            agents=False
            apply=True
            update=False
            dest=str(self.dest)
        real = kit.atomic_write
        count = 0
        def failing(path,data):
            nonlocal count
            count += 1
            if count == 2:
                raise OSError('Simulated disk write failure')
            return real(path,data)
        with patch.object(kit,'atomic_write',failing):
            with self.assertRaises(OSError):
                kit.install(Args())
        self.assertFalse(list(self.dest.rglob('SKILL.md')))

    def test_metadata_and_missing_reference_rejected(self):
        with workspace_temp() as temp:
            root = Path(temp)
            (root/'catalogo.json').write_text(json.dumps({'capacidades':[{'id':'example'}]}))
            folder = root/'skills/example'
            folder.mkdir(parents=True)
            skill = folder/'SKILL.md'
            skill.write_text('---\nname: wrong\ndescription: "Example"\n---\n',encoding='utf-8')
            with patch.object(kit,'ROOT',root):
                with self.assertRaises(ValueError): kit.validate()
                skill.write_text('---\nname: example\ndescription: "Example"\n---\n[missing](references/missing.md)\n',encoding='utf-8')
                with self.assertRaises(ValueError): kit.validate()

    def test_tampered_package_rejected(self):
        with workspace_temp() as temp:
            root = Path(temp)
            file = root/'file.txt'
            file.write_text('original')
            with patch.object(kit,'ROOT',root):
                kit.integrity(create=True)
                file.write_text('tampered')
                with self.assertRaises(ValueError): kit.integrity()

    def test_archive_is_self_contained(self):
        archive = Path(self.temp.name)/'kit.zip'
        self.run_cli('validate')
        result = subprocess.run([sys.executable,str(ROOT/'scripts/package.py'),'--output',str(archive)],capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        unpacked = Path(self.temp.name)/'unpacked'
        with zipfile.ZipFile(archive) as z:
            for item in z.namelist():
                target = (unpacked/item).resolve()
                self.assertTrue(target.is_relative_to(unpacked.resolve()))
            z.extractall(unpacked)
        copied = unpacked/'KIT-IA-UNIVERSAL/scripts/kit.py'
        result = subprocess.run([sys.executable,str(copied),'validate'],capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        result = subprocess.run([sys.executable,str(copied),'install','--profile','generic','--dest',str(self.dest),'--only','frontmd','--apply'],capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue((self.dest/'ia-kit/skills/frontmd/references/validation.md').exists())

    @unittest.skipUnless(shutil.which('git'), 'Git is not installed')
    def test_git_clone_is_self_contained(self):
        source = Path(self.temp.name)/'source'
        clone = Path(self.temp.name)/'clone'
        source.mkdir()
        manifest = json.loads((ROOT/'SHA256SUMS.json').read_text(encoding='utf-8'))
        for rel in [*manifest, 'SHA256SUMS.json']:
            target = source/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes((ROOT/rel).read_bytes())
        def git(*args):
            result = subprocess.run(['git','-c',f'safe.directory={source.as_posix()}',
                                     '-C',str(source),*args],capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
        git('init','-b','main')
        git('add','.')
        git('-c','user.name=Kit Test','-c','user.email=kit-test@example.invalid',
            '-c','commit.gpgsign=false','commit','-m','Test fixture')
        git('clone','--no-hardlinks',str(source),str(clone))
        copied = clone/'scripts/kit.py'
        result = subprocess.run([sys.executable,str(copied),'validate'],capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        result = subprocess.run([sys.executable,str(copied),'install','--profile','codex',
                                 '--dest',str(self.dest),'--only','backend-dev','--apply'],capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue((self.dest/'.agents/skills/backend-dev/references/engenharia-backend.md').is_file())

    def test_git_metadata_does_not_change_integrity(self):
        with workspace_temp() as temp:
            root = Path(temp)
            (root/'content.txt').write_text('original')
            with patch.object(kit,'ROOT',root):
                kit.integrity(create=True)
                metadata = root/'.git/config'
                metadata.parent.mkdir()
                metadata.write_text('repository metadata')
                kit.integrity()

if __name__ == '__main__':
    unittest.main()
