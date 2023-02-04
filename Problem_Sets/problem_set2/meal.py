#main function
def main():
  #ask user for input and call convert function
  timeInStr = input("what time is it: ").strip()
  time = convert(timeInStr)

  #use else if statements to see what time of day it is
  if 7.00 <= time <= 8.00:
    print("breakfast time")
  elif 12.00 <= time <= 13.00:
    print("lunch time")
  elif 18.00 <= time <= 19.00:
    print("dinner time")

#convert function takes the users input and converts it to a float
def convert(t):
  hours, mins = t.split(":")
  hours = float(hours)
  mins = float(mins) / 60

  return hours + mins


#call main function
if __name__ == "__main__":
    main()