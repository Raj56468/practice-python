def most_frequent_element(string):
    frequency = {}
    for i in string:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1   
    
    most_freqeunt = max(frequency, key=frequency.get)
    return most_freqeunt

print(most_frequent_element("banana"))      
  