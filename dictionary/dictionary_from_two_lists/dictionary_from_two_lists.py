keys = ["name", "age", "city"]
values = ["Aarav", 19, "Delhi"]
dictionary = {}

for k in keys:
    for v in values:
      dictionary.update([(k, v)])
      values.remove(v)
      break

print(dictionary)  # Output: {'name': 'Aarav', 'age': 19, 'city': 'Delhi'}

