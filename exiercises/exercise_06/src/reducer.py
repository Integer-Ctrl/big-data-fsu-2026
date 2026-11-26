#!/usr/bin/env python3

import sys

current_row = None
row_sum = 0.0

for line in sys.stdin:
    row, product = line.split()
    if row != current_row:
        if current_row is not None:
            print(f"{current_row}\t{row_sum}")
        current_row = row
        row_sum = 0.0
    row_sum += float(product)

if current_row is not None:
    print(f"{current_row}\t{row_sum}")
