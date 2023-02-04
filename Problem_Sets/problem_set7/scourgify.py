import sys
import csv


def main():
    # call a function that checks users inputted arguement
    old_filename = check_args()

    # try to open python file if it is not found exit program
    try:
        file = open(old_filename)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except OSError:
        sys.exit("Can not read file")

    # count the number of lines of code in the the program avoiding blank lines and comments
    else:
        # define line counter
        file_content = read_file(file)
        file.close()

        write_content(file_content)

        # close file and print the number of lines of code
        print("done")

# function that checka to make sure the user inputted the proper arguement with the right length


def check_args():
    # define variables used multiple times in function
    length = len(sys.argv)

    # check the number of arguements that the user inputted
    if length < 3:
        sys.exit("Too few command-line arguements")
    elif length > 3:
        sys.exit("Too many command-line arguements")

    # now check that the one arguement that the user inputted is actually a python file
    else:
        user_in = sys.argv[1]
        if user_in.endswith(".csv"):
            return user_in

        else:
            sys.exit("Not a CSV file")


def read_file(file):
    content = []
    reader = csv.DictReader(file)
    for row in reader:
        content.append(row)

    return content


def write_content(old_content):
    with open(sys.argv[2], "a") as file:

        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        for person in old_content:
            lastname, firstname = person["name"].split(", ")
            writer.writerow(
                {"first": firstname, "last": lastname, "house": person["house"]})


# call main function if program is executed
if __name__ == "__main__":
    main()
