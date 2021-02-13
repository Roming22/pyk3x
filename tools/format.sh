#!/bin/bash
echo "Format"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname $(realpath $0))"
PROJECT_DIR="$(realpath "$SCRIPT_DIR/..")"

if [[ "$#" == "0" ]]; then
    PATHS="${PROJECT_DIR}"
else
    PATHS="$@"
    for P in $PATHS; do
        [[ -e "$P" ]] || { echo "[ERROR] Path not found: $P"; exit 1; };
    done
fi

isort --profile=black ${PATHS}
black ${PATHS}

echo [OK]