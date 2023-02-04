import sys


def main():
    # call a function that checks users inputted arguement
    filename = check_args()

    # try to open python file if it is not found exit program
    try:
        file = open(filename)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # count the number of lines of code in the the program avoiding blank lines and comments
    else:
        # define line counter
        counter = 0
        for line in file:
            if line.strip().startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                counter += 1

        # close file and print the number of lines of code
        file.close()
        print(counter)


# function that checka to make sure the user inputted the proper arguement with the right length
def check_args():
    # define variables used multiple times in function
    length = len(sys.argv)

    # check the number of arguements that the user inputted
    if length < 2:
        sys.exit("Too few command-line arguements")
    elif length > 2:
        sys.exit("Too many command-line arguements")

    # now check that the one arguement that the user inputted is actually a python file
    else:
        user_in = sys.argv[1]
        if user_in.endswith(".py"):
            return user_in

        else:
            sys.exit("Not a Python file")


# call main function if program is executed
if __name__ == "__main__":
    main()
