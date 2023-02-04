#main function
def main():
  #define c and ask user for mass input
  c = 300000000
  m = int(input("Please enter the mass: "))

  #solve for energy and print
  e = m * pow(c,2)
  print("E:", e)

#call main function
main()