import random

print("Welcome in Snake Water Gun Game")
player = input("Enter your name : ")
print("In this game S -> Snake , W -> Water and G -> Gun")

try:
    times = int(input("Number of Rounds You want to play : "))
except ValueError:
    times = 5
    print("Invalid Input that's why default number of 5 rounds will be played")

dict = {
    'S' : 0,
    'W' : 1,
    'G' : 2,
    0 : 'S',
    1 : 'W',
    2 : 'G'
}

mat = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

totalScore = 0

i = 0

while i < times :
    print(f"Round {i + 1}")

    ply = input("Enter your choice from (S, W, G) : ")

    if ply not in dict:
        print("Enter a valid Input")
        continue

    computer = random.randint(0, 2)

    print(f"{player} has choosed {ply}")
    print(f"Computer has choosed {dict.get(computer)}")

    index = dict.get(ply)

    if mat[index][computer] == 0:
        print(f"It's a tie in Round {i + 1}")
    elif mat[index][computer] == 1:
        totalScore += 1
        print(f"{player} wins Round {i + 1}")
    else: 
        print(f"Computer wins Round{i + 1}")
    
    i += 1

print(f"Total score of player {player} is {totalScore}")

