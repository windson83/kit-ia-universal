#!/usr/bin/env python3
"""Offline, dependency-free installer and exporter for the capability kit (Python 3.10+)."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def read_catalog():
    data = json.loads((ROOT / 'catalogo.json').read_text(encoding='utf-8'))
    names = [c['id'] for c in data['capacidades']]
    if len(names) != len(set(names)) or not names:
        raise ValueError('Catálogo vazio ou com identificadores duplicados')
    if any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', n) or len(n) > 64 for n in names):
        raise ValueError('Identificador inválido no catálogo')
    return data

def validate():
    catalog = read_catalog()
    names = {c['id'] for c in catalog['capacidades']}
    actual = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    if actual != names:
        raise ValueError('Pastas skills divergentes do catálogo')
    for name in names:
        folder = ROOT / 'skills' / name
        skill = folder / 'SKILL.md'
        content = skill.read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', content, re.S)
        if not match:
            raise ValueError(f'{name}: frontmatter ausente')
        # This kit deliberately uses a narrow YAML subset, also valid JSON scalars.
        meta = dict(line.split(': ', 1) for line in match[1].splitlines())
        if meta.get('name') != name or not 1 <= len(json.loads(meta.get('description', '""'))) <= 1024:
            raise ValueError(f'{name}: metadados inválidos')
        for p in folder.rglob('*'):
            if p.is_symlink():
                raise ValueError(f'Link simbólico não permitido: {p}')
            if p.is_file() and p.suffix == '.md':
                text = p.read_text(encoding='utf-8')
                for link in re.findall(r'\]\(([^)]+)\)', text):
                    if '://' in link or link.startswith(('#','mailto:')):
                        continue
                    target = (p.parent / link.split('#')[0]).resolve()
                    if not target.is_relative_to(folder.resolve()) or not target.exists():
                        raise ValueError(f'{p.relative_to(ROOT)}: referência inválida: {link}')
    return catalog

def integrity(create=False):
    path = ROOT / 'SHA256SUMS.json'
    files = {p.relative_to(ROOT).as_posix(): digest(p.read_bytes())
             for p in ROOT.rglob('*') if p.is_file() and p != path
             and not any(part in {'.git', '__pycache__', '.pytest_cache', 'node_modules',
                                  'releases', '.venv'} for part in p.relative_to(ROOT).parts)
             and not p.name.endswith(('.zip', '.pyc'))}
    if create:
        path.write_text(json.dumps(files, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    else:
        expected = json.loads(path.read_text(encoding='utf-8'))
        if files != expected:
            changes = sorted(k for k in files.keys() | expected.keys() if files.get(k) != expected.get(k))
            raise ValueError('Integridade divergente: ' + ', '.join(changes))
    return len(files)

def payload(profile, selected):
    result = {}
    prefix = {'codex': '.agents/skills', 'claude': '.claude/skills', 'generic': 'ia-kit/skills'}[profile]
    for name in selected:
        folder = ROOT / 'skills' / name
        for f in sorted(folder.rglob('*')):
            if f.is_file():
                result[f'{prefix}/{name}/{f.relative_to(folder).as_posix()}'] = f.read_bytes()
    if profile == 'generic':
        catalog = read_catalog()
        catalog['capacidades'] = [c for c in catalog['capacidades'] if c['id'] in selected]
        result['ia-kit/catalogo.json'] = (json.dumps(catalog, ensure_ascii=False, indent=2) + '\n').encode()
        result['ia-kit/INSTRUCOES.md'] = (
            '# Uso em qualquer assistente\n\nLeia catalogo.json e selecione apenas a capacidade relevante. '
            'Leia skills/<id>/SKILL.md e as referências sob demanda. '
            'Se não tiver acesso a arquivos, anexe ou cole esse conteúdo na conversa. '
            'Instruções não fornecem ferramentas, execução ou agentes por si só. '
            'Respeite as instruções e permissões do ambiente.\n').encode('utf-8')
    return result

def claude_agents(selected):
    result = {}
    for name in selected:
        text = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        fields = dict(line.split(': ',1) for line in match[1].splitlines())
        desc = fields['description']
        # The skill is preloaded by Claude; supporting resources are available at its installed path.
        result[f'.claude/agents/{name}.md'] = (
            f'---\nname: {name}\ndescription: {desc}\nmodel: inherit\nskills:\n  - {name}\n---\n\n'
            f'Execute a capacidade {name} pré-carregada, respeitando o escopo delegado. '
            'Use as referências na pasta da skill instalada quando necessário. '
            'Não invente ferramentas disponíveis; registre evidências e limitações.\n').encode('utf-8')
    return result

def safe_target(root, rel):
    raw = root / rel
    # Reject both symlinks and Windows junctions in every existing component.
    current = raw
    while current != root:
        if current.is_symlink() or (hasattr(current, 'is_junction') and current.is_junction()):
            raise ValueError(f'Destino contém redirecionamento: {current}')
        current = current.parent
    target = raw.resolve()
    if not target.is_relative_to(root):
        raise ValueError(f'Destino fora da raiz: {rel}')
    return target

def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix='.kit-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as out:
            out.write(data)
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)

def install(args):
    catalog = validate()
    integrity()
    names = [c['id'] for c in catalog['capacidades']]
    selected = names if not args.only else list(dict.fromkeys(args.only))
    unknown = set(selected) - set(names)
    if unknown:
        raise ValueError('Capacidades desconhecidas: ' + ', '.join(sorted(unknown)))
    if args.agents and args.profile != 'claude':
        raise ValueError('--agents só se aplica ao perfil claude')
    root = Path(args.dest).expanduser().resolve()
    if root == ROOT or root.is_relative_to(ROOT):
        raise ValueError('Escolha um destino fora da distribuição')
    if root.exists() and not root.is_dir():
        raise ValueError('Destino deve ser diretório')
    files = payload(args.profile, selected)
    if args.agents:
        files.update(claude_agents(selected))
    plan = []
    conflicts = []
    for rel, data in files.items():
        target = safe_target(root, rel)
        parent = target.parent
        while parent != root:
            if parent.exists() and not parent.is_dir():
                raise ValueError(f'Pai do destino não é diretório: {parent}')
            parent = parent.parent
        if target.exists() and not target.is_file():
            raise ValueError(f'Destino não é arquivo: {target}')
        old = target.read_bytes() if target.exists() else None
        status = 'igual' if old == data else ('novo' if old is None else 'alterar')
        plan.append((rel, target, data, old, status))
        if status == 'alterar':
            conflicts.append(rel)
    summary = {s: sum(p[4] == s for p in plan) for s in ('novo','igual','alterar')}
    print(json.dumps({'perfil':args.profile, 'destino':str(root), 'resumo':summary,
                      'conflitos': conflicts, 'aplicar':args.apply}, ensure_ascii=False, indent=2))
    if not args.apply:
        return
    if conflicts and not args.update:
        raise ValueError('Conflitos: nenhum arquivo gravado. Revise e use --update para backup e atualização.')
    # All conflicts/paths are checked before the first mutation.
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup_rel = f'.ia-kit-backups/{stamp}'
    backup = safe_target(root, backup_rel)
    backup_plan = []
    for rel, target, data, old, status in plan:
        if status == 'alterar':
            bpath = safe_target(root, f'{backup_rel}/{rel}')
            backup_plan.append((bpath,old))
    for bpath, old in backup_plan:
        atomic_write(bpath, old)
    changed = []
    try:
        for rel, target, data, old, status in plan:
            if status != 'igual':
                # Recheck paths before writing and reject concurrent edits.
                safe_target(root, rel)
                now = target.read_bytes() if target.exists() else None
                if now != old:
                    raise ValueError(f'Destino mudou durante instalação: {rel}')
                atomic_write(target, data)
                changed.append((target,old,data))
    except Exception:
        for target, old, data in reversed(changed):
            if target.exists() and target.read_bytes() == data:
                if old is None:
                    target.unlink()
                else:
                    atomic_write(target,old)
        raise
    print(f'Instalação concluída: {len(changed)} arquivos gravados.')
    if backup_plan:
        print(f'Backup dos arquivos substituídos: {backup}')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list', help='Listar capacidades')
    check = sub.add_parser('validate', help='Validar catálogo, arquivos e hashes')
    check.add_argument('--seal', action='store_true', help='Mantenedor: regenerar hashes após revisão')
    inst = sub.add_parser('install', help='Planejar ou instalar arquivos no destino explícito')
    inst.add_argument('--profile', choices=('codex','claude','generic'), required=True)
    inst.add_argument('--dest', required=True, help='Raiz do projeto; para Claude global, diretório pessoal')
    inst.add_argument('--only', nargs='+', help='Instalar somente os identificadores informados')
    inst.add_argument('--agents', action='store_true', help='Também gerar agentes nativos do Claude')
    inst.add_argument('--apply', action='store_true', help='Efetuar gravação; sem isso é simulação')
    inst.add_argument('--update', action='store_true', help='Permitir substituir arquivos após backup')
    args = parser.parse_args()
    if args.command == 'list':
        for c in read_catalog()['capacidades']:
            print(c['id'] + ': ' + c['descricao'])
    elif args.command == 'validate':
        catalog = validate()
        count = integrity(args.seal)
        print(f'OK: {len(catalog["capacidades"])} capacidades; {count} arquivos verificados.')
    else:
        install(args)

if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('ERRO: ' + str(exc), file=sys.stderr)
        sys.exit(1)
