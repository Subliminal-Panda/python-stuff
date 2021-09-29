import random
import os
from os import system
options = ['rock', 'paper', 'scissors']
wins = [0]
losses = [0]
ties = [0]
leave = ['no','nope','none','done','leave','stop','quit','exit','finish','finished','bye','goodbye']
os.system('cls' if os.name == 'nt' else 'clear')

def rps(choice):
    def win():
        print("YOU WON!! YOU MUST HAVE CHEATED!")
        wins[0] += 1
    def lose():
        print("YOU LOST, YA GOOF!!")
        losses[0] += 1
    def tie():
        print("It's a tie... boring.")
        ties[0] += 1
    def comp_chose():
        print(f'The computer chose: {comp_choice.upper()}\n')

    comp_choice = options[random.randint(0,len(options)-1)]
    choice = choice.lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == 's':
        choice = 'scissors'
    if choice == 'r':
        choice = 'rock'
    if choice == 'p':
        choice = 'paper'
    print(f'You chose: {choice.upper()}\n')
    
    if choice == '' or choice == ' ' or choice == '  ':
            print('Uh... you didn\'t enter a choice.')
            
    elif choice == 'rock':
        comp_chose()
        if comp_choice == 'paper':
            lose()
        elif comp_choice == 'scissors':
            win()
        else:
            tie()
        options.append('paper')
        
    elif choice == 'paper':
        comp_chose()
        if comp_choice == 'scissors':
            lose()
        elif comp_choice == 'rock':
            win()
        else:
            tie()
        options.append('scissors')
        
    elif choice == 'scissors':
        comp_chose()
        if comp_choice == 'rock':
            lose()
        elif comp_choice == 'paper':
            win()
        else:
            tie()
        options.append('rock')

    elif choice in(leave):
        print('It\'s been fun!')

    else:
        print('I didn\'t understand your choice. Check your spelling maybe?')
    
    scoreboard = (f'Wins: {wins} Losses: {losses} Ties: {ties}')

    if choice not in(leave):
        print(f'\n{scoreboard}')
        print('\nTry your luck again?\n')
        rps(input('Your choice:'))
    else:
        print(f'\nYour final score: {scoreboard}\n\nBye!')


rps(input('Let\'s play rock-paper-scissors!\nEnter your choice:'))