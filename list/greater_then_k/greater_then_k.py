nums = [1, 5, 7, 2, 10]
k = 4

greater_then_k = []
count = 0

for num in nums:
    if k < num:
        count += 1
        greater_then_k.append(num)
        
print(count, greater_then_k)
