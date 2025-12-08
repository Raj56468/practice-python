from collections import Counter

def find_most_frequent_element(lst):
    frequency = Counter(lst)
    print(dict(frequency))


find_most_frequent_element([2,2,3,1])