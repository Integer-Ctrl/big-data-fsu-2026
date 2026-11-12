#!/bin/bash

python preprocessing.py

# cat Data/cleaned/regional_averages_tm_*.txt | python mapper.py | python reducer.py > Data/results.txt
cat Data/cleaned/regional_averages_tm_*.txt | python mapper.py | python shuffel.py |python reducer.py
