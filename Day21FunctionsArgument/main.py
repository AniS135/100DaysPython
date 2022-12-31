# # Default Argument
# def average(a = 9, b = 1):
#     print("The average is ", (a + b) / 2)

# # Required Argument(a in below example)
# def average(a, b = 1):
#     print("The average is ", (a + b) / 2)


# # Keyword Argument
# average(b= 3, a = 21)

# Variable length Argument

def average(*num) :
    sum = 0
    for i in num : 
        sum = sum + i

    return sum / len(num)

c = average(3, 7)
print(c)

# Keyword Arbitary Argument

def name(**name):
    print("Hello", name["fname"], name["mname"], name["lname"])

name(fname = "James", lname = "Barnes", mname = "Buchana")
