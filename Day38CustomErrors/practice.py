a = input("Enter any value between 5 and 9 :")

class CustomError(Exception) :
    "Raised when the input value is less than 5 or greater than 9"
    pass


try : 
    a = int(a)
    if(a < 5 or a > 9):
        raise CustomError
except ValueError:
    if(a != "quit") : 
        raise ValueError("Entered value is a string")

except CustomError:
    print("Value should be between 5 ans 9")
