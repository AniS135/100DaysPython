marks = [12, 54, 5, 24 , 5, 22, 24, 63, 54, 12]

# enumerate function -> gives a tuple first is index and second is value

for index, mark in enumerate(marks, start = 1):
    print(mark)
    if(index == 3):
        print("Aniket, awesome!")

