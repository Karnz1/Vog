import random

def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user():
    guess = int(input("Please guess a number: "))
    return guess

def compare_results(random_number, guess):
    if random_number == guess:
        return True
    else:
        return False

def play():
    generate_number()
    get_guess_from_user()
    return compare_results()