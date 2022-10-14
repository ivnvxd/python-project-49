import prompt


def greet():
    ''' Greet the user and get his name '''

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".''')

    return name


def question(ask):
    ''' Ask the question '''

    print(f'Question: {ask}')


def answer():
    ''' Get the guess from user '''

    answer = prompt.string('Your answer: ')
    return answer


def check(guess, correct, correct_answers, name):
    ''' Check if the user's answer equals correct one '''

    if guess == correct:
        print('Correct!')

        # Increase correct answers counter
        correct_answers += 1
        return correct_answers
    else:
        wrong(guess, correct, name)


def wrong(guess, correct, name):
    ''' Prints guess and correct answers and closes the program '''

    print(f"'{guess}' is wrong answer ;(.", end=' ')
    print(f"Correct answer was '{correct}'.")
    print(f"Let's try again, {name}!")

    # Close the program if wrong answer provided
    quit()
