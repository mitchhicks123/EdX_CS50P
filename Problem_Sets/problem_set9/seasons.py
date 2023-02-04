from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    # ask user for input
    today = date.today()
    dob = birth_date(input("Date of Birth: ").strip())


    difference = get_difference(today, dob)

    print(output(difference))
    sys.exit()

# validate that user's date of birth input is in correct format otherwise raise a ValueError
def birth_date(dob):

    try:
        year, month, day = dob.split("-", 2)
        year = int(year)
        month = int(month)
        day = int(day)
        birth_date = date(year, month, day)

    except ValueError:
        raise ValueError

    else:
        return birth_date

# get the difference between todays date and users Birthdate... convert to mins


def get_difference(today, birth_date):
    difference = today - birth_date
    difference_in_mins = difference.days * 24 * 60
    return difference_in_mins

# take in the minutes numerically and covert to words to produce final string
def output(mins):
    final = p.number_to_words(mins).replace(" and", "") + " minutes"
    return final.capitalize()


if __name__ == "__main__":
    main()
