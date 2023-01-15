# a = input("Enter the number: ")
# print(f"Muliplication table of {a} is: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a) * i}")

# except Exception as e:
#     print("Invalid Input!")

# print("Some imp lines of code")
# print("End of program")

try :
    a = int(input("Enter the number: "))
    num = [6, 3]
    print(num[a])
    
except ValueError:
    print("Entered number is not a integer.")

except IndexError:
    print("Index Error")