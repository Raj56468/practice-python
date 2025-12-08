def find_second_largest(lst):
    largest = max(lst)
    lst.remove(largest)
    second_largest = max(lst)
    return second_largest

print(find_second_largest([1, 2, 3, 4, 5]))
