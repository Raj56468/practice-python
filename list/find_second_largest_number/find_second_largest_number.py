nums = [5, 1, 9, 3, 7]

largest_num = 0
second_largest_num = 0

for n in nums:
    if largest_num < n:
        largest_num = n
    elif second_largest_num < n:
        second_largest_num = n  

print("Second largest number is:", second_largest_num)
