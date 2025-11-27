d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}

new_dict = {}

for d in (d1, d2):
   new_dict = {**new_dict, **d}

print(new_dict)