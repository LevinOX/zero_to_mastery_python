""" Run from the command line typing
    python .\guessing_game.py 1 10
"""

import sys
from random import randint

first = int(sys.argv[1])
last = int(sys.argv[2])
number = randint(first, last)
print(number)
while True:
    try:
        guess = int(
            input(f"guess a number from {sys.argv[1]} to {sys.argv[2]}: "))
        if guess == number:
            print(f"well done, the correct answer is {number}!")
            break
        elif first <= guess <= last:
            print("all good, but - please try again")
            continue
        else:
            print("out of bounds - please try again")
    except ValueError:
        print("please enter a value")
