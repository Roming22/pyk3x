#!/bin/bash
echo "Setup"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

find "${SCRIPT_DIR}" -mindepth 2 -name setup.sh | while read -r SETUP; do
    echo "$SETUP"
    echo "=> $(basename "$(dirname "${SETUP}")")"
    $SETUP
    echo "<=  $(basename "$(dirname "${SETUP}")")"
    echo
done

echo "[OK]"