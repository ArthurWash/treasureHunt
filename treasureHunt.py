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


def enter_cave():
    pass


def main_loop():
    display_game_intro()
    cave_input = choose_cave()
    print('you chose cave ' + cave_input)


main_loop()
