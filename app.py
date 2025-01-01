def welcome():
    name = input("Enter your name: ")
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")

def start_play():
    game = input("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    difficulty = input("Please choose the difficulty between 1 and 5 ")


