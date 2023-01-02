l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

# add element in last
l.append(7) 
print(l)

# sort list
l.sort() 
print(l)

# sort list in reverse order
l.sort(reverse= True) 
print(l)

# Reverse original list
l.reverse()
print(l)

# Returns the index of first occurance of the list item
print(l.index(1))
print(l)

# Return the count/frequency of list item
print(l.count(1))
print(l)

# Creates a copy of a list
m = l.copy()
m[0] = 0
print(l)

# Inser element at given position
l.insert(1, 899)
print(l)

# Append m to original list
m = [900, 1000, 1100]
k = l + m
k[0] = 0
print(k)
# l.extend(m)
print(l)

