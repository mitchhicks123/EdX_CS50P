import re
import sys


def main():
    user_in = " " + input("Text: ").strip() + " "
    num = count(user_in)
    print(num, end="")


def count(s):
    list_matches = re.findall(r"\bu[m]+\b", s, re.IGNORECASE)
    num = len(list_matches)
    return num

if __name__ == "__main__":
    main()
