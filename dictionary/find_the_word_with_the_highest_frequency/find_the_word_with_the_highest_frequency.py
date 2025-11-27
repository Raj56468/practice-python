words = ["apple", "banana", "apple", "orange", "banana", "apple"]

words_with_highest_frequency = {}
highest_freq = {}

for w in words:
    if w in words_with_highest_frequency:
        words_with_highest_frequency[w] += 1
    else:
        words_with_highest_frequency[w] = 1
    
for word, freq in words_with_highest_frequency.items():
    if freq not in highest_freq:
        highest_freq[freq] = [word]
    else:
        highest_freq[freq].append(word)

print(highest_freq[max(highest_freq)])



# Alternative way

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

max_word = ""
max_count = 0

for word in words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        max_word = word

print(max_word)
