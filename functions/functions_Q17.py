def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

# Example usage
print(running_total([1, 2, 3, 4]))  


