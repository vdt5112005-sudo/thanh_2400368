#!/bin/bash
F="$(dirname "$0")/../../Sanpham/banggia.csv"
echo "So dong: $(wc -l < "$F")"
echo "So ky tu: $(wc -m < "$F")"
