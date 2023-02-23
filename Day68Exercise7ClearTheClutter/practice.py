import os
import random
import string

# Enter the directory path according to your pc.
path = "C:\\Users\\AS\\Documents\\PythonHelp\\"

dir_list = os.listdir(path)

ext = input("Enter the extension name : ")
ext = ext.lower()

count = 1

for files_name in dir_list:
    if files_name.endswith(f".{ext}") :
        try :
            os.rename(path + files_name , path + f"{count}.{ext}")
        except :
            pass
        count = count + 1

if count == 1:
    print(f"File with extension {ext} doesn't exist in the directory.")
else : 
    print(f"Files names with extension {ext} are changed Successfully")


