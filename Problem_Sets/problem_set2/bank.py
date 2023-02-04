#main function
def main():
  #ask user for input and strip whitespace and convert to lower case
  userIn = input("Greeting: ").lower().strip()

  #check to see if they greeted them with "hello"
  if "hello" in userIn:
    print("$0")

  #check to see if they greeted them with "h"
  elif userIn[0] == "h":
    print("$20")

  #otherwise they get $100
  else:
    print("$100")


#call the main function
main()