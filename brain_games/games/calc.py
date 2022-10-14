from random import randrange, choice
from ..engine import greet, question, answer, check, wrong


def calc():
    # Greet the user and get his name
    name = greet()

    # Count correct answers
    correct_answers = 0

    # Set list of used operators
    ops = ['+', '-', '*']

    # Use functions in a dictionary
    operator_functions = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }

    # Continue until 3 correct answers in a row
    while correct_answers < 3:

        # Generate two random numbers from 1 to 19
        a = randrange(1, 20)
        b = randrange(1, 20)

        # Choose a random operator
        operator = choice(ops)

        # Calculate correct answer
        correct = operator_functions[operator](a, b)

        # Ask game's question
        ask = f"{a} {operator} {b}"
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
