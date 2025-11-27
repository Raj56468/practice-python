nums = [2, 3, 2, 4, 3, 2]

frequency= {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
        continue
    else:
        frequency[num] = 1

print(frequency)