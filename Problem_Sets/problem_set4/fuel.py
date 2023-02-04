
#main function
def main():
    #call check fuel
  fraction = check_fuel("Fuel Gauge: ")
    #check the returned value of the check fuel function
  if  fraction >= .99:
    print("F")

  elif fraction <=.01:
    print("E")

  else:
    print(int(fraction * 100), "%", sep="")


#this function checks the fuel and returns a decimal
def check_fuel(prompt):
  while True:
    #ask user for input
    try:
      x, y = input(prompt).split("/", 1)
      x = int(x)
      y = int(y)
    #if the user doesn't input a number... then prompt them again
    except ValueError:
      pass

    else:
      try:
        decimal = x / y
    #if the user enters a zero for y then prompt them again
      except ZeroDivisionError:
        pass

      else:
        if y >= x:
          return round(decimal, 2)

#call main function
main()