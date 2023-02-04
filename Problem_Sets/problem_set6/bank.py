
# Problem 2: Home Federal Savings Bank


def main():
    userIn = input("Greeting: ")
    print("$", value(userIn))


def value(greeting):
    greeting = greeting.lower().strip()

    if greeting == "hello":
        return 0

    elif greeting[0] == "h":
        return (20)

    else:
        return 100


if __name__ == "__main__":
    main()
