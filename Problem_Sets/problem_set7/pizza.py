import sys
import csv
from tabulate import tabulate


def main():
    # call a function that checks users inputted arguement
    filename = check_args()

    # try to open python file if it is not found exit program
    try:
        file = open(filename)
    except FileNotFoundError:
        sys.exit("File does not exist")

    else:
        menu = []
        # implement dictreader with the header as the first dictionary element
        reader = csv.reader(file)

        for pizza_type, small_cost, large_cost in reader:
            menu.append({"type": pizza_type,
                         "small": small_cost, "large": large_cost})
    file.close()
    print(tabulate(menu, tablefmt="grid"))


def check_args():
    # define variables used multiple times in function
    length = len(sys.argv)

    # check the number of arguements that the user inputted
    if length < 2:
        sys.exit("Too few command-line arguements")
    elif length > 2:
        sys.exit("Too many command-line arguements")

    # now check that the one arguement that the user inputted is actually a csv file
    else:
        user_in = sys.argv[1]
        if user_in.endswith(".csv"):
            return user_in
        else:
            sys.exit("Not a CSV file")


# call main function if program is executed
if __name__ == "__main__":
    main()
