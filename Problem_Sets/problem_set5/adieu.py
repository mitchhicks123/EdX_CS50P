
#main function
def main():
    #call function to get user inputted names
    list_of_names = get_input()
    print("\nAdieu, adieu, to " + printed_string(list_of_names))

#function to get the list of names from the user
def get_input():
    names = []
    while True:
        try:
            #add names to list
            names.append(input("Name: "))
        except EOFError:
            return names

#function that takes in names and returns the properly formated string
def printed_string(children_names):
    final_string = ""
    #fix function
    if len(children_names) == 1:
        return children_names[0]

    if len(children_names) == 2:
        return children_names[0] + " and " + children_names[1]

    for name in children_names[:-1]:
        final_string += name + ", "

    return final_string + "and " + children_names[len(children_names)-1]

#call main function
main()
