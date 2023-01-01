# A List can store different data type members
# Indexing starts from 0 to len-1

marks = [3, 5, 6, "Aniket", True, 6, 7, 2, 4, 14, 1343]

# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3])
# print(marks[len(marks) - 3])

# if "6" in marks :
#     print("Yes")
# else :
#     print("No")
# Same thing applies for string
# if "Ha" in "Harry":
#     print("Yes")

# print(marks)
# print(marks[1:-1])
# print(marks[1 : len(marks) - 1: 2])
# # arr[::x] here x roles as jump index basically we will jump to i + x index

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)




