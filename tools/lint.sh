#!/bin/bash
echo "Lint"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/..")"

run_pylint(){
    for DIR in src tests; do
        echo "=> pylint ${PROJECT_DIR}/${DIR}"
        pylint --rcfile="${SCRIPT_DIR}/pylintrc.${DIR}" "${PROJECT_DIR}/${DIR}"
    done
    echo

}

run_shellcheck(){
    echo "=> shellcheck"
    find "${PROJECT_DIR}" -name \*.sh -exec shellcheck {} \;
    echo
}

run_pylint
run_shellcheck
echo [OK]