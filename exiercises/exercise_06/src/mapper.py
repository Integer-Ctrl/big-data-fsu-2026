#!/usr/bin/env python3

import sys


for line in sys.stdin:
    row, value, x = line.split()
    product = float(value) * float(x)
    print(f"{row}\t{product}")
