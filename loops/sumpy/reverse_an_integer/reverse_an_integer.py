n = int(input("Enter a non-negative integer: "))

rev = 0

while n>0:
    digit = n % 10
    rev = rev*10 + digit
    n = n // 10

print("Reversed integer:", rev)