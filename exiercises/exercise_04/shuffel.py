import sys

data = []

for line in sys.stdin:
    year, temp = line.strip().split('\t', 1)
    data.append((year, temp))

sorted_data = sorted(data, key=lambda x: x[0])

for year, temp in sorted_data:
    print(f"{year}\t{temp}")
