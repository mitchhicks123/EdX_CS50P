#main function
def main():

  #insert 3 periods for every whitespace in the str and then print the results
  userIn = input("What would you like to say? ")
  userIn = userIn.replace(" ", "...")

  print (userIn)

#call main function
main()