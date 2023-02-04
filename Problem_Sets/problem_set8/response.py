from validator_collection import checkers


def main():
    print(checker(input("Email: ")))


def checker(user_in):
    result = checkers.is_email(user_in)
    if result == True:
        return "Valid"

    else:
        return "Invalid"


if __name__ == "__main__":
    main()
