""" Run from the command line typing
    python .\guessing_game.py 1 10
"""

import sys
from random import randint

FIRST = 1  # int(sys.argv[1])
LAST = 10  # int(sys.argv[2])


def guess_fcn(number, answer, first, last):
    if not isinstance(answer, int):
        return False
    if answer == number:
        print(f"well done, the correct answer is {number}!")
        return True
    elif first <= answer <= last:
        print("all good, but - please try again")
        # return False
    else:
        print("out of bounds - please try again")
        # return False


# print("wrong answer: ", guess_fcn(5, 0, 1, 10))


def ask_input(first, last):
    return int(
        input(f"guess a number from {first} to {last}: "))


if __name__ == '__main__':
    NUMBER = randint(FIRST, LAST)
    print(NUMBER)

    while True:
        try:
            guess = ask_input(FIRST, LAST)
            if guess_fcn(NUMBER, guess, FIRST, LAST):
                break
        except ValueError:
            print("please enter a value")
