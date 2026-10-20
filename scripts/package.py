#!/usr/bin/env python3
"""Create a self-contained ZIP from the sealed manifest, without legacy dependencies."""
import argparse
import json
from pathlib import Path
import zipfile
import kit

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Default: releases/kit-ia-universal-<version>.zip')
    args = parser.parse_args()
    catalog = kit.validate()
    kit.integrity()
    version = catalog['versao']
    dest = (args.output or kit.ROOT / 'releases' / f'kit-ia-universal-{version}.zip').resolve()
    if dest.exists():
        raise ValueError('Arquivo já existe; escolha outro --output para preservar a versão anterior')
    members = json.loads((kit.ROOT/'SHA256SUMS.json').read_text(encoding='utf-8'))
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED) as archive:
        for rel in sorted([*members, 'SHA256SUMS.json']):
            path = kit.ROOT/rel
            info = zipfile.ZipInfo('KIT-IA-UNIVERSAL/' + rel, date_time=(2026,10,20,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (0o100755 if rel.endswith('.sh') else 0o100644) << 16
            archive.writestr(info,path.read_bytes())
    print(dest)

if __name__ == '__main__':
    main()
