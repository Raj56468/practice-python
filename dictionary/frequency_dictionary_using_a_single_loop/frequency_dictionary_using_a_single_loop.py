nums = [1, 1, 2, 3, 3, 3]
freq_dict = {}
for num in nums:
    freq_dict[num] = freq_dict.get(num, 0) + 1

print(f"Input: {nums}")
print(f"Output: {freq_dict}")