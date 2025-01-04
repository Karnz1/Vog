import random

EXCHANGE_RATE = 3.65

def get_money_interval():
    return random.randint(1, 100)


def get_guess_from_user():
    guess = int(input("Please guess the value of the amount in USD: "))
    return guess

def compare_results(random_number, guess):
    if random_number == guess:
        return True
    else:
        return False
    
def play():
    get_money_interval()
    get_guess_from_user()
    return compare_results()