#main function
def main():
    #ask user for dollar input
    dollars = dollars_to_float(input("How much was the meal? "))
    #ask user for percent input
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #calculate and print tip
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#function that takes the users input and coverts to float for dollars
def dollars_to_float(d):
  d = d.replace("$", "")
  return float(d)

#function that takes the users input and coverts to float for percentage
def percent_to_float(p):
  p = p.replace("%","")
  p = float(p)
  return (p/100)

#call main function
main()