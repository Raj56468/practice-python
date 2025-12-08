def returns_only_even_numbers(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers     

print(returns_only_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
