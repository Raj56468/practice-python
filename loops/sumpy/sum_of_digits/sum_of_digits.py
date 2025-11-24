n = int(input("Enter a non-negative integer: "))

total = 0

while n>0:
    last_digit = n % 10  # get the last digit
    total += last_digit  # add it to total
    n = n // 10          # remove the last digit

print("The sum of the digits is:", total)