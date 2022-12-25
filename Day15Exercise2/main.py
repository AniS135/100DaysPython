import time

t = time.localtime()

current_time = t.tm_hour

if(current_time < 12):
    print("Good Morning Sir")
elif(current_time < 16):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")