# for i in range(12):
#     if(i == 10):
#         print("Skip the iteration") 
#         continue
#     print("5 X", i, "=", 5 * (i))

# print("End of loop")

for i in [2,3,4,5,7,6,8] : 
    if(i % 2 == 1): continue
    print(i, end=" ")

print()

for i in [2,4,3,6,8,10,12]:
    if(i % 2 == 1): break
    print(i, end=" ")