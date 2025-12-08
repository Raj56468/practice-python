def find_max_num(num_list):
    # Handle the edge case of an empty list to prevent an error.
    if not num_list:
        return None

    # Initialize a variable to hold the maximum value, starting with the first element.
    max_value = num_list[0]
    
    # Iterate through each number in the list.
    for num in num_list:
        # If the current number is greater than our stored maximum, update it.
        if num > max_value:
            max_value = num
            
    return max_value

print(find_max_num([1, 2, 3, 4, 5]))