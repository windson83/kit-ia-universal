#!/usr/bin/env sh
set -eu
KIT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$KIT_DIR/scripts/kit.py" "$@"
