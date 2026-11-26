#!/bin/bash
set -o pipefail
cd -- "$(dirname -- "$0")" || exit 1

# m n density
uv run sparse_matrix_vector_product.py "$@" 4 4 0.5

shopt -s nullglob
cat data/*.txt </dev/null | python3 mapper.py | LC_ALL=C sort -k1,1n | python3 reducer.py
