"""1st roll wins on 7, 11 -- loses on 2, 3, 12 -- store any other roll
rolls after that stored roll wins -- loses on 7 -- keep rolling on anything else"""
import random

def diceRoll():
    return random.randint(1,6)

def craps():
    """1st Roll"""
    die1, die2 = diceRoll(), diceRoll()
    firstRoll=die1+die2
    print(f'Welcome to craps \nWith a {die1} and a {die2} you rolled a {firstRoll}')
    if firstRoll in [7, 11]:
        print('You Win!')
    if firstRoll in [2,3,12]:
        print('You Lose.')
    if firstRoll not in [2, 3, 7, 11, 12]:
        subsequentRoll = 0
        while(firstRoll != subsequentRoll and subsequentRoll != 7):
            die1, die2 = diceRoll(), diceRoll()
            subsequentRoll=die1+die2
            input(f'point. You must roll a {firstRoll} to win. Press Enter to roll.')
            print(f'\nWith a {die1} and a {die2} you rolled a {subsequentRoll}')
        if firstRoll == subsequentRoll:
            print('You Win!')
        if subsequentRoll == 7:
            print('You Lose.')
    """Subsequent Rolls"""

craps()
