# factorial(n) = factorial(n - 1) * n
# factorial(0) = 1

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


# fibonacci series
# f(n) = f(n - 1) + f(n - 2)
# f(0) =0
# f(1) =1

def fib(n) :
    if(n == 0 or n == 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))