""" Run from the command line typing
    python .\guessing_game.py 1 10
"""

import sys
from random import randint

FIRST = int(sys.argv[1])
LAST = int(sys.argv[2])
NUMBER = randint(FIRST, LAST)
print(NUMBER)


def guess_fcn(number, inp, first, last):
    if inp == number:
        print(f"well done, the correct answer is {number}!")
        return True
    elif first <= inp <= last:
        print("all good, but - please try again")
        # continue
    else:
        print("out of bounds - please try again")


def ask_input(first, last):
    return int(
        input(f"guess a number from {first} to {last}: "))


while True:
    try:
        guess = ask_input(FIRST, LAST)
        if guess_fcn(NUMBER, guess, FIRST, LAST):
            break
    except ValueError:
        print("please enter a value")
