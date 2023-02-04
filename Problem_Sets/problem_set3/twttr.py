# Problem 3: Twttr

#main function
def main():
    #get user input
    user_in = input("Input: ")
    output = ""

    #loop through each character and check whether or not it is a vowel... if it is do not add it to new string
    for letter in user_in:
        character = letter.lower()

        if character in ["a", "i", "e", "o", "u"]:
            continue
        else:
            output += letter
    #output new string without vowela
    print("Output: " + output)

#call main function
main()
