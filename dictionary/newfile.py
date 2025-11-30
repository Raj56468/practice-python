word = "banana"
vowels = "aeiou"
freq = {}

for ch in word:
    if ch in vowels:
        freq[ch] = freq.get(ch, 0) + 1

print(freq)

