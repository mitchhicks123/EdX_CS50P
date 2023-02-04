import random
import sys

#main function
def main():
    difficulty_level = get_level()
    guessing(difficulty_level)

#function that gets the user inout for the level of difficulty
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                return level

#this function runs the game and compares users guesses to the actually value
def guessing(difficulty):
    random_number = random.randint(0, difficulty)

    while True:
        guess_value = ask_guess(difficulty)

        if guess_value > random_number:
            print("Too Large!")

        elif guess_value < random_number:
            print("Too Small!")

        else:
            print("Just Right!")
            sys.exit()

# function that gets users guesses and validates that it is a proper input
def ask_guess(level):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if 0 <= guess <= level:
                return guess

#call main function
main()
