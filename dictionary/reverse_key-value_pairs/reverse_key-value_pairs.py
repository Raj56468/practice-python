d = {"a": 1, "b": 2, "c": 3}


rev = {}
for k, v in d.items():
    rev[v] = k
print(rev)
