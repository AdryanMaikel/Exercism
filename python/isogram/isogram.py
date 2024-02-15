import re


def is_isogram(string: str) -> bool:
    """Check if string is a isogram.
    :param string: str - String to checked.
    :return: bool - If is a isogram.
    """
    letters = []
    for letter in string:
        letter = letter.lower()
        if letter in letters and re.match(r"[a-zA-Z]", letter):
            return False
        letters.append(letter)
    return True
