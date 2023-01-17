a = int(input("Enter any value between 5 and 9 :"))

# We use raise keyword to generate custom errors
if(a < 5 or a > 9):
    raise ValueError("Value should be between 5 ans 9")

# We can also use custom exception to raise error rather just using inbuilt exceptions

# class CustomError(Exception):
#     #code
#     pass

# try : 
#     # Code
# except CustomError:
#     # Code