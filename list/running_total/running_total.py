nums = [2, 4, 6, 1]

running_total = []

for nun in nums:
    if running_total:
        running_total.append(running_total[-1] + nun)
    else:
        running_total.append(nun)
print("Running total is:", running_total)