
# CONFUSED ABOUT THIS ONE, trying coding this one yourself again

import random


user_choosed_pos = []      # defining variables for the players choosing position
player1_choosed_pos = []
player2_choosed_pos = []

# For computer
computer_pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']    # defining how many positions there are on the board


def first_printing():   # printing board
    print('Here is the positions\n')
    print('    |     |      \n 1  |  2  |   3\n    |     |      ')
    print('_ _ _ _ _ _ _ _ _\n')
    print('    |     |      \n 4  |  5  |   6\n    |     |      ')
    print('_ _ _ _ _ _ _ _ _\n')
    print('    |     |      \n 7  |  8  |   9\n    |     |      \n')


def printing_view():    #
    pos1 = pos2 = pos3 = pos4 = pos5 = pos6 = pos7 = pos8 = pos9 = '-'

    for i in player1_choosed_pos:      # putting an x for where the users chooses
        if i == '9':
            pos9 = 'X'
        elif i == '8':
            pos8 = 'X'
        elif i == '7':
            pos7 = 'X'
        elif i == '6':
            pos6 = 'X'
        elif i == '5':
            pos5 = 'X'
        elif i == '4':
            pos4 = 'X'
        elif i == '3':
            pos3 = 'X'
        elif i == '2':
            pos2 = 'X'
        elif i == '1':
            pos1 = 'X'

    for i in player2_choosed_pos:    # the computer
        if i == '9':
            pos9 = 'O'
        elif i == '8':
            pos8 = 'O'
        elif i == '7':
            pos7 = 'O'
        elif i == '6':
            pos6 = 'O'
        elif i == '5':
            pos5 = 'O'
        elif i == '4':
            pos4 = 'O'
        elif i == '3':
            pos3 = 'O'
        elif i == '2':
            pos2 = 'O'
        elif i == '1':
            pos1 = 'O'

    print('\n')     # reprint the board after the moves
    print(f'    |     |      \n {pos1}  |  {pos2}  |   {pos3}\n    |     |      ')
    print('_ _ _ _ _ _ _ _ _\n')
    print(f'    |     |      \n {pos4}  |  {pos5}  |   {pos6}\n    |     |      ')
    print('_ _ _ _ _ _ _ _ _\n')
    print(f'    |     |      \n {pos7}  |  {pos8}  |   {pos9}\n    |     |      \n')


# Game over when all position choosen and no one has won
def game_over():
    game_over_ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    game_over_ls2 = []
    for i in game_over_ls:
        if i in user_choosed_pos:
            game_over_ls2.append(i)

    return game_over_ls == game_over_ls2


def points_scored():        # if they won, the positions on the board
    # For Player 1
    if ('1' in player1_choosed_pos) and ('2' in player1_choosed_pos) and ('3' in player1_choosed_pos):
        return True
    elif ('1' in player1_choosed_pos) and ('4' in player1_choosed_pos) and ('7' in player1_choosed_pos):
        return True
    elif ('7' in player1_choosed_pos) and ('8' in player1_choosed_pos) and ('9' in player1_choosed_pos):
        return True
    elif ('3' in player1_choosed_pos) and ('6' in player1_choosed_pos) and ('9' in player1_choosed_pos):
        return True

    elif ('1' in player1_choosed_pos) and ('5' in player1_choosed_pos) and ('9' in player1_choosed_pos):
        return True
    elif ('3' in player1_choosed_pos) and ('5' in player1_choosed_pos) and ('7' in player1_choosed_pos):
        return True
    elif ('2' in player1_choosed_pos) and ('5' in player1_choosed_pos) and ('8' in player1_choosed_pos):
        return True
    elif ('4' in player1_choosed_pos) and ('5' in player1_choosed_pos) and ('6' in player1_choosed_pos):
        return True

        # For Player 2
    if ('1' in player2_choosed_pos) and ('2' in player2_choosed_pos) and ('3' in player2_choosed_pos):
        return True
    elif ('1' in player2_choosed_pos) and ('4' in player2_choosed_pos) and ('7' in player2_choosed_pos):
        return True
    elif ('7' in player2_choosed_pos) and ('8' in player2_choosed_pos) and ('9' in player2_choosed_pos):
        return True
    elif ('3' in player2_choosed_pos) and ('6' in player2_choosed_pos) and ('9' in player2_choosed_pos):
        return True

    elif ('1' in player2_choosed_pos) and ('5' in player2_choosed_pos) and ('9' in player2_choosed_pos):
        return True
    elif ('3' in player2_choosed_pos) and ('5' in player2_choosed_pos) and ('7' in player2_choosed_pos):
        return True
    elif ('2' in player2_choosed_pos) and ('5' in player2_choosed_pos) and ('8' in player2_choosed_pos):
        return True
    elif ('4' in player2_choosed_pos) and ('5' in player2_choosed_pos) and ('6' in player2_choosed_pos):
        return True

    # Frontend


player1 = input('Type fist player name: ').title()              # getting the input from the user
computer_playing = input('Want to play with computer (Y/N): ').strip().lower()[:1]

if computer_playing == 'n':     # if they say no no playing against the computer
    player2 = input('Type Second player name: ').title()
elif computer_playing == 'y':
    player2 = 'computer'

player1_sign = 'X'
player2_sign = 'O'

if computer_playing == 'n':     # player 1 and 2
    print(
        f'Welcome {player1} your sign "{player1_sign}".\nWelcome {player2}. your sign "{player2_sign}".\nBest of luck\n')

elif computer_playing == 'y':   # player 1 and computer
    print(f'Welcome {player1} your sign "{player1_sign}".\nComputer\'s sign "{player2_sign}".\nBest of luck\n')

user_said = input('Want to play (Y/N): ').strip().lower()[:1]   # dont understand the last part

while True:
    if 'y' in user_said:
        first_printing()

        while True:     # the input of the player
            position = input(f'{player1} type position: ')

            if position:    # calling the functions from above
                user_choosed_pos.append(position)
                player1_choosed_pos.append(position)
                computer_pos.remove(position)

            printing_view()     # printing board

            if game_over() or points_scored():      # the user output if they've won
                if points_scored():
                    print(f'Congrats {player1}. You won.\n')
                else:
                    print('Sorry all position choosen. No one won :(')

                user_said = input('Play more (Y/N): ').strip().lower()[:1]
                if 'n' in user_said:
                    print('Ok bye. see you soon.')
                    break   # stopping the game

                elif 'y' in user_said:
                    user_choosed_pos = []
                    player1_choosed_pos = []
                    player2_choosed_pos = []
                    computer_pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    continue        # continue the game

            if computer_playing == 'y':         # random generator for number
                random.shuffle(computer_pos)    # random position
                position = random.choice(computer_pos)  # defining the variable
                print(f'Computer choose position: {position}')  # telling the player what the computer chose
            else:
                position = input(f'{player2} type position: ')  # everything else is what player 2 put in

            if position:
                user_choosed_pos.append(position)       # .append() adds a single item to the existing list
                player2_choosed_pos.append(position)
                computer_pos.remove(position)

            printing_view()

            if game_over() or points_scored():
                if points_scored():
                    print(f'Congrats {player2}. You won.\n')
                else:
                    print('Sorry all position choosen. Noone won :(')

                user_said = input('Play more (Y/N): ').strip().lower()[:1]
                if 'n' in user_said:
                    print('Ok bye. see you soon.')
                    break
                elif 'y' in user_said:
                    user_choosed_pos = []
                    player1_choosed_pos = []
                    player2_choosed_pos = []
                    computer_pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    continue

    elif 'n' in user_said:
        break
    else:
        user_said = input('wrong keyword.Type again: ').strip().lower()[:1]
