from random import randrange
from ..engine import greet, question, answer, check


def game():
    # Greet the user and get his name
    name = greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Count correct answers
    correct_answers = 0

    # Continue until 3 correct answers in a row
    while correct_answers < 3:

        # Generate random number from 0 to 99
        number = randrange(0, 100)

        # Calculate correct answer
        correct = even(number)

        # Ask game's question
        ask = f"{number}"
        question(ask)

        # Get user's answer
        guess = answer()

        # Check if the user's answer equals correct one
        correct_answers = check(guess, correct, correct_answers, name)

    # Check if user made 3 correct answers in a row (not necessary)
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


def even(number):
    ''' Check if generated number is even or odd '''

    if number % 2 == 0:
        return 'yes'  # Number is even
    else:
        return 'no'  # Number is odd
