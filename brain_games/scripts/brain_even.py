import prompt
from random import randrange


def main():
    # Greet the user and get his name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Count correct answers
    correct_answers = 0

    while correct_answers < 3:

        # Generate a random number from 1 to 99
        number = randrange(1, 100)

        # Check if generated number is even or odd
        if number % 2 == 0:
            correct = 'yes'  # Number is even
        else:
            correct = 'no'  # Number is odd

        # Ask user for answer
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        # Check if the user's answer equals correct one
        if answer == correct:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end='')
            print(f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")

            # Quit if wrong answer provided
            quit()

    # Check if user made 3 correct answers in a row
    # (this check is not necessary because of quit()
    # function after a wrong answer)
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
