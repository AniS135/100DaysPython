# Strings are immutable

a = "!!Aniket!!!!Aniket!!!!!"

print(len(a))

print(a)

print(a.upper()) # Create new string with uppercase letter
print(a.lower()) # Create new string with lowercase letter

print(a.rstrip("!")) # Create new string after removing trailing characters

print(a.replace("Aniket", "Saini")) # Create new string after replacing all occurance of first string with second

print(a.split("!")) # Create a list by spliting the string

heading = "introduction tO pYTHON"

print(heading.capitalize()) # Create new string with first character in capital and all other in lowercase

str = "Welcome to Console!!!"
# print(str.center(50)) # Add spaces in front of string
print(len(str))
print(len(str.center(50)))

print(a.count("Aniket")) # Tells the frequency of asked string in original string

str = "Welcome to Console !!!"

print(str.endswith("!!!")) # Tells whether the given string ends with a particular string or not
print(str.endswith("to", 4, 10)) # Same as above but in given substring
print(str.startswith("Welcome")) # Same as above but in given substring

str = "HesnameisDom"

print(str.find("ishh")) # return index of first occurance of given string in original string. If not found it returns -1
print(str.index("is")) # return index of first occurance of given string in original string But if not found it shows error

print(str.isalnum()) # returns true if string contains character from A-Z, a-z, 0-9 otherwise(" ", "!", punctuations) false

str = "Aniket03" 
print(str.isalpha()) # returns true if string only contains alphates(A-Z, a-z) otherwise return false

str = "hello world"
print(str.islower()) # if all character are in lower case then return true
print(str.isupper()) # if all character are in upper case then return true

str = "Nice to meet you\n"
print(str.isprintable()) # return true if string is printable

str = "       "
print(str.isspace()) # if string only contains white space then returns true

str = "World health Organization"
print(str.istitle()) # returns true only if first character of each word is capital

print(str.swapcase()) # converts all upper case letter to lower case and visa versa

str = "I aM a HONEST Man"
print(str.title()) # Converts given string in title format


