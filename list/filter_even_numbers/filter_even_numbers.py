nums = [1, 2, 3, 4, 5, 6]

even_num = []

for n in range(len(nums)):
    if nums[n] % 2 == 0:
        even_num.append(nums[n])
    

print(even_num)



#alternative way
number = [1, 2, 3, 4, 5, 6]

even_numbers = []

for num in number:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)