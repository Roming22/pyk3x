#!/bin/bash
echo "Format"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/../..")"

OPTIONS=()
PATHS=()
while [[ "$#" -gt "0" ]]; do
    case $1 in
        --check)
            OPTIONS+=( "$1" )
            ;;
        *)
            [[ -e "$1" ]] || { echo "[ERROR] Path not found: $1"; exit 1; };
            PATHS+=( "$1" )
            ;;
    esac
    shift
done
[[ -n "${PATHS[*]}" ]] || PATHS+=( "$PROJECT_DIR" )
isort --profile=black "${OPTIONS[@]}" "${PATHS[@]}"
black "${OPTIONS[@]}" "${PATHS[@]}"

echo [OK]