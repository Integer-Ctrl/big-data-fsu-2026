#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # get year from first column
    year = words[0]
    for word in words[1:]:
        print('%s\t%s' % (year, word))
    