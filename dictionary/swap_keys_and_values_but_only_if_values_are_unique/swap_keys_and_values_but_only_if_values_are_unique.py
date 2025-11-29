# python
from collections import Counter

data = {"a": 1, "b": 2, "c": 1, "d": 3}

value_counts = Counter(data.values())

swapped = {}
for k, v in data.items():
    if value_counts[v] == 1:    # value is unique -> include swapped pair
        swapped[v] = k

print(swapped)  # output: {2: 'b', 3: 'd'}