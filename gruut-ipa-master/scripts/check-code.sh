#!/usr/bin/env bash
set -e

# Directory of *this* script
this_dir="$( cd "$( dirname "$0" )" && pwd )"
src_dir="$(realpath "${this_dir}/..")"

venv="${src_dir}/.venv"
if [[ -d "${venv}" ]]; then
    source "${venv}/bin/activate"
fi

python_files=("${src_dir}/gruut_ipa/"*.py "${src_dir}/setup.py")
python_files+=("${src_dir}/tests/"*.py)

# -----------------------------------------------------------------------------

flake8 "${python_files[@]}"
pylint "${python_files[@]}"
mypy "${python_files[@]}"
black --check "${python_files[@]}"
isort --check-only "${python_files[@]}"

# -----------------------------------------------------------------------------

echo "OK"
