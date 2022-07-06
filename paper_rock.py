from random import randint

print('You choose? Paper, Scissor or Rock')

player = input()
mai = randint(0,2)
if mai == 0:
    mai = "Paper"
if mai == 1:
    mai = "Scissor"
if mai == 0:
    mai = "Rock"

print('---')
print('You choose: '+ str(player))
print('Computer chooses: '+  str(mai))
print("---")

if player == mai:
    print('Draw')
else:
    if player == "Scissor":
        if mai == "Paper":
            print("Win")
        else:
            print("Loose")
    elif player == 'Rock':
        if mai == "Scissor":
            print("Win")
        else:
            print("Loose")
    else:
        if mai == 'Rock':
            print('Win')
        else:
            print('Loose')
           
print(" Enter 'Quit' to exit the game")
if input() == "Quit":
    print('Thanks for playing with me')
    exit()

            







