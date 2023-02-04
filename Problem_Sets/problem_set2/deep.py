#main function
def main():
    #ask user for input and convert to lowercase
  userIn = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

  #check is users input is 42 in different versions
  if userIn in["42", "forty two", "forty-two"]:
    print ("Yes")
  else:
    print ("No")


#call main function
main()