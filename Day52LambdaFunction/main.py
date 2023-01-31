# def double(x):
#     return x * 2

# Passing function to a function
def appl (fx, value):
    return 6 + fx(value)

# Lambda function mainly used for one liner
double = lambda x : x * 2
cube = lambda x : x ** 3
avg = lambda x, y, z : (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
# Anonymous function
print(appl(lambda x : x * x, 2))