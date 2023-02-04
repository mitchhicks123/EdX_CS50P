
# Problem 1: Fuel Gauge


def main():
    user_in = input("Fuel Gauge: ")
    fraction = convert(user_in)
    print(gauge(fraction))


def convert(fraction):

    x, y = fraction.split("/", 1)
    x = int(x)
    y = int(y)

    # put else in a seperate function to ease readability
    percent = int((x / y) * 100)

    if y >= x:
        return percent

    else:
        raise ValueError


def gauge(percentage):
    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
