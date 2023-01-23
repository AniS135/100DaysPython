import string
import random

while(True) :
    command = input("Enter 'Code' to code the word or \n'Decode' to decode the word or \n'Exit' if you don't want to code or decode : ")
    if(command == 'Code'):
        str = input("Enter the word you want to code or decode : ")
        if(len(str) < 3):
            print(str[::-1])
        else:
            ans = str[-1:] + str[:-1]
            front = ''.join(random.choices(string.ascii_lowercase, k=3))
            end = ''.join(random.choices(string.ascii_lowercase, k=3))
            print(front + ans + end)
    elif(command == 'Decode'):
        str = input("Enter the word you want to code or decode : ")
        if(len(str) < 3):
            print(str[::-1])
        else:
            removedExtra = str[3 : -3]
            ans = removedExtra[1:] + removedExtra[:1]
            print(ans)
    elif(command == 'Exit'):
        break
    else:
        print("Invalid String Input")


    