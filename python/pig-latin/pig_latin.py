VOWELS = ["a", "e", "i", "o", "u"]


def translate_word(word: str) -> str:
    """Translates each word of the text.
    :param word: str - Word to translate.
    :return: str - Word translated.
    """
    if word[0] in VOWELS or word.startswith("xr") or word.startswith("yt"):
        return f"{word}ay"

    if "qu" in word:
        partition = word.partition("qu")
        return f"{''.join(partition[2:])}{''.join(partition[0:2])}ay"

    if "y" in word[0:2]:
        partition = "".join(reversed(word.partition("y")))
        return f"{partition}ay"

    if word[1] in VOWELS:
        partition = word.partition(word[1])
        return f"{word[1:]}{word[0:1]}ay"

    if len(word) > 2:
        if word[2] in VOWELS or word[2] == "y":
            return f"{word[2:]}{word[0:2]}ay"

    return f"{word[3:]}{word[0:3]}ay"


def translate(text: str) -> str:
    """Function that translates from English to Pig Latin.
    :param text: str - Text to translate.
    :return: str - Text translated to Pig Latin.
    """
    words = text.split(" ")
    return " ".join([translate_word(word) for word in words])
