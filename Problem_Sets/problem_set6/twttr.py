# Problem 3: Twttr

def main():
    user_in = input("Input: ")
    print(shorten(user_in))


def shorten(word):
    output = ""
    for letter in word:
        character = letter.lower()

        if character in ["a", "i", "e", "o", "u"]:
            continue
        else:
            output += letter

    return output


if __name__ == "__main__":
    main()
