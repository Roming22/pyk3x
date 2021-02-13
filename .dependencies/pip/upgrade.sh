#!/bin/bash
echo "Upgrading pip packages"
set -e
set -o pipefail
SCRIPT_DIR="$(dirname $(realpath $0))"

FROZEN="$SCRIPT_DIR/frozen.txt"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"

pip freeze | xargs --no-run-if-empty pip uninstall -y
pip install -r "${REQUIREMENTS}"

pytest "$SCRIPT_DIR/../../tests"

pip freeze > "$SCRIPT_DIR/frozen.txt"

echo "[OK]"