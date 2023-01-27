x = 4

print(x)

# Global keyword is used to access global variable in a function

def hello():
    global x
    x = 5
    print(f"The local x is {x}")
    print("******************")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")