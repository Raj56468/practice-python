nums = [3, 3, 4, 2, 3, 3, 5]

majority_element = {}

for num in nums:
    if num in majority_element:
        majority_element[num] += 1
    else:
        majority_element[num] = 1

print(majority_element)

majority_element_count = 0
majority_element_value = 0

for key, value in majority_element.items():
    if value > majority_element_count:
        majority_element_count = value
        majority_element_value = key

print(majority_element_value)