# Problem 4: Vanity Plates
import string


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper().strip()
    checker = False

    # check length of plate..... 2 <= plate <= 6
    if len(s) > 6 or len(s) < 2:
        return False

    # check if first two characters are letters
    if s[:2].isalpha() == False:
        return False

    for letter in s[2:]:
        # if the license plate includes punctuation marks (look at taking string punctuation)
        if letter in string.punctuation:
            return False

        # check that the first number used isn't a zero
        # as soon as a number is hit just check to see if the remaining characters are numeric
        if checker == False and letter == "0":
            return False

        # check that numbers only appear at the end of the license plate and not in the middle
        if letter.isalpha() and checker:
            return False

        if letter.isnumeric():
            checker = True

    return True


if __name__ == "__main__":
    main()
