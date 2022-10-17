from random import randrange
from ..engine import greet, question, answer, check


def game():
    # Greet the user and get his name
    name = greet()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # Count correct answers
    correct_answers = 0

    # Continue until 3 correct answers in a row
    while correct_answers < 3:

        # Generate random number from 0 to 99
        number = randrange(0, 100)

        # Calculate correct answer
        correct = is_prime(number)

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


# Implement instead of math.gcd() function
def is_prime(number):
    ''' Check if given number is prime or not '''

    # If given number is greater than 1
    if number > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(number / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                return 'no'
        else:
            return 'yes'
    else:
        return 'no'
