#!/usr/bin/env python

from operator import itemgetter
import sys

current_year = None
current_year_temp_sum = 0
current_year_temp_count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    year, temp = line.split('\t', 1)

    # convert temp (currently a string) to float
    try:
        temp = float(temp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_year == year:
        current_year_temp_sum += temp
        current_year_temp_count += 1
    else:
        if current_year:
            # write result to STDOUT
            print('%s\t%s' % (current_year, current_year_temp_sum / current_year_temp_count))
        current_year = year
        current_year_temp_sum = temp
        current_year_temp_count = 1

# do not forget to output the last word if needed!
if current_year == year:
    print('%s\t%s' % (current_year, current_year_temp_sum / current_year_temp_count))

