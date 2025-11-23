n = 0
while n <= 0:
    try:
        n = int(input("Enter a positive integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        n = 0

total = 0
for i in range(1, n + 1):
    total += i

print(f"Sum from 1 to {n} is {total}")

