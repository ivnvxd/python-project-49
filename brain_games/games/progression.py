from ..engine import greet, question, answer, check, wrong
from random import randrange


def game():
    # Greet the user and get his name
    name = greet()
    print('What number is missing in the progression?')

    # Count correct answers
    correct_answers = 0

    # Continue until 3 correct answers in a row
    while correct_answers < 3:

        # Generata a random progression length from 7 to 14 items
        length = randrange(7, 14)

        # Generate a random starting number for the progression from 0 to 20
        first = randrange(0, 21)

        # Generate a random step in the progression from 1 to 10
        step = randrange(1, 11)

        # Generate question position from 0 to progression length
        position = randrange(0, length)

        # Generate whole progression and calculate correct answer
        progression, correct = get_progression(length, first, step, position)

        # Ask game's question
        ask = f"{progression}"
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


def get_progression(length, first, step, position):
    progression = ''
    current_number = first

    # Iterate through progression length and add numbers
    for i in range(length):

        if i == position:

            # Save correct answer and change it to '..' instead
            correct = current_number
            progression += '..' + ' '

        else:
            progression += str(current_number) + ' '

        current_number += step

    return progression, correct
