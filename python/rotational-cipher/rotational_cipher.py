def rotate(text: str, key: int) -> str:
    """Function that rotates the alphabet passing a number to be
    incremented in the index.
    :param text: str - Text to be replaced.
    :param key: int - Number to be incremented from the letter index in
    the alphabet.
    :return: str - New text rotated.
    """
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    chars = []
    for digit in text:
        if digit.isalpha():
            index = ALPHABET.index(digit.lower()) + key
            char = ALPHABET[index if index < 26 else index - 26]
            chars.append(char if digit.islower() else char.upper())
        else:
            chars.append(digit)
    return "".join(chars)
