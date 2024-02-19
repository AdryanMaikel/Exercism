ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    NEW_ALPHABET = {}
    for i, j in enumerate(range(26)):
        j = j + key
        if j >= 26:
            j -= 26
        NEW_ALPHABET[i + 1] = ALPHABET[j]
    print(NEW_ALPHABET)

    # indexes = [i for i, letter in enumerate(ALPHABET) if letter in text]
    # NEW_ALPHABET = [ALPHABET[(i + key) % 26] for i in range(26)]
    # return "".join([NEW_ALPHABET[index] for index in indexes])


rotate("", 0)
