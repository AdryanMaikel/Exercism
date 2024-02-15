import re


def is_pangram(sentence: str) -> bool:
    """Check if sentence is pangram, pangram is a sentence that contains
    all the letters alphabet.
    :param sentence: str - Sentence to check if it is pangram.
    :return: bool - If is pangram.
    """
    alphabet = r'[a-zA-Z]'
    letters = []
    for letter in sentence:
        letter = letter.lower()
        if re.match(alphabet, letter) and letter not in letters:
            letters.append(letter)
    return True if len(letters) == 26 else False
