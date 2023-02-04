# Problem 1: Camel Case

#main function
def main():
    #take input from the user
    camel_case = input("camelCase: ")
    snake_case = ""

    #loop through the string... if the letter is upper case than must be the start of a new word
    for letter in camel_case:
        if letter.isupper():
            snake_case = snake_case + "_" + letter.lower()

        else:
            snake_case += letter

    print("snake_case:", snake_case)

#call main function
main()
