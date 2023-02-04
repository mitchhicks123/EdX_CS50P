#main function
def main():
  #ask user for input
  userIn = input("Expression: ").strip()
  # x y z , where x and z are floats and y is an operator
  x, y, z = userIn.split(" ")
  x = float(x)
  z = float(z)

  #check to see what operation is need using an else if statement
  if y == "+":
    print(x + z)
  elif y == "-":
    print(x - z)
  elif y == "*":
    print(x * z)
  else:
    print(x/z)

#call main function
main()
