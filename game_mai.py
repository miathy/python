from random import randint
def play():
    print('---')
    print("Welcome to the game. Let's start!")
    print('You choose? Paper, Scissor or Rock')

    player = input()
    mai = randint(0,2)
    if mai == 0:
        mai = "Paper"
    if mai == 1:
        mai = "Scissor"
    if mai == 2:
        mai = "Rock"
    
    print('---')
    print('You choose: ' + player)
    print('Mai chooses: ' + mai)
    print("---")

    if player == mai:
        print('Draw')
    else:
        if player == "Scissor":
            if mai == "Paper":
                print("Congrats! You win")
            else:
                print("Haha: Loose")
        elif player == 'Rock':
            if mai == "Scissor":
                print("Congrats! You win")
            else:
                print("Haha: Loose")
        else:
            if mai == 'Rock':
                print('Congrats! You win')
            else:
                print('Haha: Loose')
   
while True:   
    answer = input("Enter 'Next' to play or 'Quit' to exit the game:  ")
    print('')
    if answer == 'Next':
        play()
    elif answer == 'Quit':
        print('Thanks for playing with me')
        break
    else:
        print('Please enter again!')

    

    







