 Given a non-negative integer, calculate the sum of its digits.
for example, input 1234, output 4321

To get the last digit of a number we can use modulus operator % 10
To remove the last digit of a number we can use integer division // 10

total = 0
while number > 0:
    last_digit = number % 10
    total += last_digit
    number = number // 10
print(total)