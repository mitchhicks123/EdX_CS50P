import sys
from PIL import Image, ImageOps


def main():
    # call a function that checks users inputted arguement
    input_file, output_file = check_args()

    # try to open python file if it is not found exit program
    try:
        image1 = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # count the number of lines of code in the the program avoiding blank lines and comments
    else:
        # define line counter
        image2 = Image.open("shirt.png")
        overlay_image(image1, image2, output_file)

        # close file and print the number of lines of code
        image1.close()
        image2.close()
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

        extensions = (".jpg", ".jpeg", ".png")
        # split on the dot and you do -1 (get the last instance in the file) and use "in" keyword
        user_in = sys.argv[1].lower()
        user_out = sys.argv[2].lower()
        in_extension = "." + user_in.split(".")[-1]
        out_extension = "." + user_out.split(".")[-1]

        if in_extension in extensions[0:1] and out_extension in extensions[0:1]:
            return user_in, user_out

        elif in_extension in extensions[2] and out_extension in extensions[2]:
            return user_in, user_out

        elif (in_extension in extensions and out_extension in extensions) == False:
            sys.exit("Invalid Input")

        else:
            sys.exit("Input and Output have different extensions")


def overlay_image(background, shirt, output_name):
    background = ImageOps.fit(background, size=(600, 600))
    background.paste(shirt, mask=shirt)
    background.save(output_name)


# call main function if program is executed
if __name__ == "__main__":
    main()
