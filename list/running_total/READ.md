Running Total (Prefix Sum Style)

Given a list, return a new list where:

each element is the sum of all elements up to that index.

Example:

nums = [2, 4, 6, 1]
# step sums:
# index 0: 2           → 2
# index 1: 2+4   = 6   → 6
# index 2: 2+4+6 = 12  → 12
# index 3: 2+4+6+1=13  → 13
# output: [2, 6, 12, 13]

Pattern:

Use running = 0

For each num:

running += num

append running to a new list