import random
import sys

#main function
def main():
    score = 0
    #call function to get users input
    difficulty_level = get_level()

    #start game by looping through 10 questions using for loop
    for _ in range(10):
        #create x and y values for math question
        x_value, y_value = generate_integer(difficulty_level)
        #check answer
        score += check_answer(x_value, y_value)

    print(f"Score: {score}")
    sys.exit()

#get users inout for difficulty of the game... verify its a valid input
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level


#function that generates 2 numbers
def generate_integer(level):
    # 10 to the power of level'
    end_val = (10 ** level) - 1
    start_val = 10 ** (level - 1)

    if level == 1:
        start_val = 0
    #get random integer for math question based on level
    x = random.randint(start_val, end_val)
    y = random.randint(start_val, end_val)

    return x, y

#check the users input compared to the correct answer... give them 3 attempts
def check_answer(x, y):
    for _ in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            pass
        else:
            if answer == (x + y):
                return 1

        print("EEE")

    print(f"{x} + {y} =", x + y)
    return 0

#call main function
if __name__ == "__main__":
    main()
