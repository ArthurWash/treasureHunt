# Python Treasure Hunt Game

import random, time


def display_game_intro():
    print('''
            Welcome to the 'Python Treasure Hunt Game'!
            A game created to help me reinforce the foundations of Python.
            
            After a long journey, you find yourself in front of two caves.
            One cave leads to a treasure, while the other has a spike filled pit.
            Being you, the player, are a brave treasure hunter looking to pay off a debt,
            you decide to take the risk!
        ''')


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave do you want to enter? (1 or 2)')
        cave = input()
    return cave


def enter_cave(chosen_cave):
    print('You entered the cave.')
    time.sleep(1)

    random_cave = random.randint(1, 2)
    print()

    if random_cave == int(chosen_cave):
        print('Lucky you! You found the chest!')
    else:
        print('You expected to find a chest...but you fall to your death into a spike pit :(')


def main_loop():
    ''' The main_loop() function controls the flow of the game by
    calling functions and using conditionals'''

    play_game_again = 'yes'

    while play_game_again == "yes" or play_game_again == "y":
        display_game_intro()
        chosen_cave = choose_cave()
        enter_cave(chosen_cave)

        print('\n\nDo you want to try again? (yes or no)')
        play_game_again = input()
        print('You entered: ' + play_game_again)
        time.sleep(1)

        if play_game_again == 'yes' or play_game_again == 'y':
            print('\nGreat! Lets try again!')
            time.sleep(1)
        else:
            print('\nNo worries, cya next time!')


main_loop()
