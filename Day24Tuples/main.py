tup = (1, 2, 76, 543, 32, "Green", True)
# tup[0] = 90
print(type(tup), tup)
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[5])

if 32 in tup:
    print("Yes 32 present in this tuple")

tup2 = tup[1 : 4]
print(tup2)
print(tup)