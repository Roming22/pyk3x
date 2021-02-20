#!/bin/bash
echo "Update coverage"
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/../../..")"

set -x
generate(){
    "${SCRIPT_DIR}/../../test.sh" "${PROJECT_DIR}/tests/src" || true
    cp "${SCRIPT_DIR}/report.txt" "${SCRIPT_DIR}/report.ref"
}

generate
echo "[OK]"