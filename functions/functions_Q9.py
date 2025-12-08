def check_if_string_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
print(check_if_string_palindrome("madam"))
print(check_if_string_palindrome("hello"))
