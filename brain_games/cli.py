import prompt


def welcome_user():
    """Asking for the user's name"""
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
