import time

def usingWhile():
    i = 0
    while i < 50000:
        i = i + 1

def usingFor():
    for i in range(50000):
        continue

init = time.time()
usingFor()
print(time.time() - init)

init = time.time()
usingWhile()
print(time.time() - init)

print(4)
time.sleep(3)
print("This is printed after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)