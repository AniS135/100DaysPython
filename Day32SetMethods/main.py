s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# Union of two sets
print(s1.union(s2))
s1.update(s2) # Add all elements of s2 which is not present in s1
s1 = s1.union(s2)

# Intersections of two sets
s3 = s1.intersection(s2)
s1.intersection_update(s2)
print(s1)

# Symmetric_difference = union - intersections
s3 = s1.symmetric_difference(s2)
print(s3)

# Difference a.diff(b) = a - b
s3 = s1.difference(s2)
print(s3)

# isdisjoint is True if two sets don't have any common elements
s3 = s1.isdisjoint(s2)
print(s3)

# a.issuperset(b) is true if all the elements of b are also present in a
s3 = s1.issuperset(s2)
print(s3)

# a.issubset(b) is true if all elements of a are present in b
s3 = s1.issubset(s2)
print(s3)

# add -> to add item in a set
s1.add(10)
print(s1)

# remove/discard -> remove a element from a set
# remove -> it gives error if element is not present in a set
s1.discard(1)
print(s1)

# pop -> it removes random element from set(from last)
item = s1.pop()
print(s1)
print(item)

# # del -> delete entire set 
# del s1

# clear -> remove all elements of a set 
s1.clear()

# in -> to check a number present in a set

if 1 in s1:
    print("hello")