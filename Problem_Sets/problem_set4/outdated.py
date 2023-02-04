
#main function
def main():
    #define a list of months
  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]

  print (sort_date(months))


def sort_date(months_list):
    #get input from user with month... if not in the proper
  while True:
    user_in = input("Date: ").strip().capitalize()
    try:
        #convert the users date input to integers... for date format 1
      month, day, year = user_in.split("/",2)
      month = int(month)
      day = int(day)
      year = int(year)

    except ValueError:
      try:
        #convert the users date input to integers... for date format 2
        month, day_year = user_in.split(" ",1)
        day, year = day_year.split(", ",1)
        day = int(day)
        year = int(year)

      except ValueError:
        pass

      #if values are within the acceptable date ranges then return formated string
      else:
        if month in months_list and 0 < day <= 31:
          month = months_list.index(month) + 1
          return format_date(year, month, day)

    #if values are within the acceptable date ranges then return formated string
    else:
      if 0 < month <= 12 and 0 < day <= 31:
        return format_date(year, month, day)


#format date into string
def format_date(year, month, day):
    year = str(year).zfill(4)
    month = str(month).zfill(2)
    day = str(day).zfill(2)

    return year + "-" + month + "-" + day


#call main function
main ()
