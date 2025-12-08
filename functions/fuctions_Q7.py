def remove_duplicates(lst):
    set1 = set(lst)
    unique_list = list(set1)
    unique_list.sort()
    return unique_list

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))