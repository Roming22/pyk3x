#!/bin/bash
echo "Upgrading pip packages"
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

FROZEN="${SCRIPT_DIR}/requirements.txt"
PACKAGES="${SCRIPT_DIR}/packages.txt"

pip freeze | xargs --no-run-if-empty pip uninstall -y
pip install -r "${PACKAGES}"

pytest "${SCRIPT_DIR}/../../tests"

pip freeze > "${FROZEN}"

echo "[OK]"