#!/bin/bash
echo "Lint"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/../..")"

parse_args(){
    LINTERS=()
    while [[ "$#" -gt "0" ]]; do
        case $1 in
            --*)
                LINTERS+=( "$(echo "$1" | cut -c3-)" )
                ;;
        esac
        shift
    done

    if [[ -z "${LINTERS[*]}" ]]; then
        for LINTER in "pylint" "shellcheck"; do
            LINTERS+=( "${LINTER}" )
        done
    fi
}

run_pylint(){
    for DIR in src tests; do
        echo "=> pylint ${PROJECT_DIR}/${DIR}"
        pylint --rcfile="${SCRIPT_DIR}/pylintrc.${DIR}.ini" "${PROJECT_DIR}/${DIR}"
    done
    echo

}

run_shellcheck(){
    echo "=> shellcheck"
    find "${PROJECT_DIR}" -name \*.sh -print0 | xargs --no-run-if-empty --null shellcheck
    echo
}

parse_args "$@"
for LINTER in "${LINTERS[@]}"; do
    "run_${LINTER}"
done
echo [OK]
