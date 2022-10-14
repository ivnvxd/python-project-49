from random import randrange
# from math import gcd
from ..engine import greet, question, answer, check, wrong


def game():
    # Greet the user and get his name
    name = greet()

    # Count correct answers
    correct_answers = 0

    # Continue until 3 correct answers in a row
    while correct_answers < 3:

        # Generate two random numbers from 2 to 99
        a = randrange(2, 100)
        b = randrange(2, 100)

        # Calculate correct answer
        correct = gcd(a, b)

        # Ask game's question
        ask = f"{a} {b}"
        question(ask)

        # Get user's answer
        guess = answer()

        # Check if provided answer is an integer and convert it
        try:
            guess = int(guess)
        except ValueError:
            wrong(guess, correct, name)

        # Check if the user's answer equals correct one
        correct_answers = check(guess, correct, correct_answers, name)

    # Check if user made 3 correct answers in a row (not necessary)
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


# Implement instead of math.gcd() function
def gcd(a, b):
    ''' Find greatest common divisor of the two integers '''

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return (a + b)
