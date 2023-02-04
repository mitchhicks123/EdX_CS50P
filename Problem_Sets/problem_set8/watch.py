import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(
        r"src=\"http(?:s)?://(?:www.)?youtube\.com/embed/([a-zA-Z0-9]+)\"", s)
    if matches:
        return f"https://youtu.be/" + matches.group(1)
    else:
        return "none"


if __name__ == "__main__":
    main()
