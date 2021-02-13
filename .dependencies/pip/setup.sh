#!/bin/bash
set -e
set -o pipefail
SCRIPT_DIR="$(dirname $(realpath $0))"

FROZEN="$SCRIPT_DIR/frozen.txt"
pip install -r "${FROZEN}"
