ep1 = {
    122 : 45,
    123 : 89,
    567: 69,
    670: 69
}

ep2 = {
    222 : 67,
    566 : 90
}

# Update
ep1.update(ep2)
print(ep1)

# # Clear all key value pairs
# ep1.clear()
# print(ep1)

empt = {}
print(empt)

# Pop -> remove a pair whoose key is given
ep1.pop(122)
print(ep1)

# Pop Item -> Removes the last element from dict
ep1.popitem()
print(ep1)

# del ep1
# del ep1[122]

print(ep1)