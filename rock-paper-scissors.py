import random

while True:

    Player_Choices = ['ROCK', 'PAPER', 'SCISSORS']
    Player_Input = input('Rock, Paper, Scissors, SHOOT! ')
    while Player_Input.upper() not in Player_Choices:
        print('Please enter one of the three choices given...')
        Player_Input = input('Rock, Paper, Scissors, SHOOT! ')

    System_Choices = ['Rock', 'Paper', 'Scissors']
    System_Input = random.choice(System_Choices)
    print('Computer: ' + System_Input)

    Draw = False
    Win_Condition = 0

    if Player_Input.upper() == 'ROCK':
        if System_Input == 'Scissors':
            Win_Condition = True
        if System_Input == 'Paper':
            Win_Condition = False
        if System_Input.upper() == Player_Input.upper():
            Draw = True

    if Player_Input.upper() == 'SCISSORS':
        if System_Input == 'Paper':
            Win_Condition = True
        if System_Input == 'Rock':
            Win_Condition = False
        if System_Input.upper() == Player_Input.upper():
            Draw = True

    if Player_Input.upper() == 'PAPER':
        if System_Input == 'Rock':
            Win_Condition = True
        if System_Input == 'Scissors':
            Win_Condition = False
        if System_Input.upper() == Player_Input.upper():
            Draw = True

    if Win_Condition is True:
        print('Congrats! You Win!')
    if Win_Condition is False:
        print('Dang, You Lost...')
    if Draw is True:
        print("It's a Draw")

    Replay = input("Want to play again? Yes or No: ")
    if Replay.upper() == 'NO':
        break

print('Bye!')
