n = int(input("enter numbers: "))

c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0

while n > 0:
    last_digit = n%10
    
    if last_digit == 0:
        c0 += 1
    elif last_digit == 1:
        c1 += 1 
    elif last_digit == 2:
        c2 += 1
    elif last_digit == 3:
        c3 += 1 
    elif last_digit == 4:
        c4 += 1
    elif last_digit == 5:
        c5 += 1
    elif last_digit == 6:
        c6 += 1
    elif last_digit == 7:
        c7 += 1
    elif last_digit == 8:
        c8 += 1
    elif last_digit == 9:
        c9 += 1
    n = n // 10
    
print(f"0:", c0)
print(f"1:", c1)
print(f"2:", c2)
print(f"3:", c3)
print(f"4:", c4)
print(f"5:", c5)
print(f"6:", c6)
print(f"7:", c7)
print(f"8:", c8)
print(f"9:", c9)
        
