#import library
import emoji

#main function
def main():
    #Take user input and turn it into an emoji
    user_in = input("Input: ")
    print("Output: " + emoji.emojize(user_in, language="alias"))

#call main function
if __name__ == "__main__":
    main()
