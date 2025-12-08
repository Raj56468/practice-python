def find_common_elements(list1, list2):
    a = set(list1)
    b = set(list2)
    c = a.intersection(b)
    return list(c)

print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
