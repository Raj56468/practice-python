def if_anagram(string1, string2):
     if sorted(string1) == sorted(string2):
          return True
     else:
          return False
     
print(if_anagram("listen", "silent"))
print(if_anagram("hello", "world"))

      
    