n = int(input("Enter a non-negative integer: "))

count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
sum_of_powers = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** count
    temp //= 10
if sum_of_powers == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
    