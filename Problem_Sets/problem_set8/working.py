import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matches = re.search(
        r"^([1-9]|[1][0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|[1][0-2])(:[0-5][0-9])? (AM|PM)$", s)

    if matches == None:
        raise ValueError

    else:
        final_shift = get_24hr(matches.group(1), matches.group(2), matches.group(
            3)) + " to " + get_24hr(matches.group(4), matches.group(5), matches.group(6))

        return final_shift


def get_24hr(hours, mins, period):

    time_24hr = ""
    if period == "AM":
        if hours == "12":
            hours = "00"

        if mins == None:
            # make new function for zfill and appending
            time_24hr = str(hours).zfill(2) + ":00"
        else:
            time_24hr = str(hours).zfill(2) + mins

    else:
        if hours != "12":
            hours = int(hours) + 12

        if mins == None:
            time_24hr = str(hours) + ":00"
        else:
            time_24hr = str(hours) + mins

    return time_24hr


if __name__ == "__main__":
    main()
