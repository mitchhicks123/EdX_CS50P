import pyfiglet
import sys
#import librarys

#main function
def main():
    # get number of command line arguement
    arg_length = len(sys.argv)
    #if command line arguements = 1 then there were no command line arguements past in
    if arg_length == 1:
        user_in = input("Input: ")
        print(pyfiglet.Figlet().renderText(user_in))
        exit(0)

    #call function that verfies command line arguements passed in by the user
    num_inputs = command_line(arg_length)
    user_in = input("Input: ")
    print(num_inputs.renderText(user_in))

#function that verifies command line arguements
def command_line(length):

    if length != 3 or sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid Usage")

    try:
        font_object = pyfiglet.Figlet(sys.argv[2])
    except Exception:
        sys.exit("Invalid Usage")
    else:
        return font_object


main()
