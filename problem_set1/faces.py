#main function
def main():
  #ask user for input
  userIn = input("What would you like to say? ")
  print (convert(userIn))


#function that converts emoticons to emojis
def convert(text):
  text = text.replace(":)", "🙂").replace(":(", "🙁")
  return text

#call main function
main()