n = int(input("Enter a non-negative integer: "))

rev = 0

while n > 0:
    last_digit = n % 10
    rev = rev * 10 + last_digit
    n = n // 10
    if n == rev or n // 10 == rev:
        print("The number is a palindrome.")
        break
    elif n < rev:
        print("The number is not a palindrome.")
        break