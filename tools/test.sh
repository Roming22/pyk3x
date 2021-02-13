#!/bin/bash
echo "Test"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/..")"

run_pytest(){
    echo "=> pyltest ${PROJECT_DIR}/tests"
    pytest -n 4 "${PROJECT_DIR}/tests"
    echo

}

run_pytest
echo [OK]
