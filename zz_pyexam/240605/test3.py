

data = { 'name': 'a', 'age': 12, 'email': 'aaa@example.com' }

print([(a, b) for a, b in data.items()])
# print([a, b for a, b in data.items()])
# print([a, b for a, b in data])
# print([(a, b) for a, b in data])