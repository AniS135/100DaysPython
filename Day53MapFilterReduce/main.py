# MAP

# cube = lambda x : x ** 3

l = [1, 2, 4, 6, 2, 3]
# newl = []

# for item in l:
#     newl.append(cube(item))

# Map each value of list with new element
# Input Sequence of Element
# Output Sequence of Element
# Higher Order Function(Function is given as argument)
newl = list(map(lambda x : x ** 3, l))
print(newl)


# FILTER

# Takes function and iterable
# if functions return true then this element is added in final list else not


# filter_function = lambda a : a > 2
newnewl = list(filter(lambda a : a > 2, l))

print(newnewl)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda a,b : a + b , numbers)

print(sum)

