#!/bin/bash
echo "Package"; echo
set -e
set -o pipefail
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PROJECT_DIR="$(realpath "${SCRIPT_DIR}/../..")"
cd "${PROJECT_DIR}"

check-manifest --ignore '.devcontainer/**,dependencies/**,src/__init__.py,tests/**,tools/**'

echo [OK]