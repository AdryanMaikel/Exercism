def translate(text: str) -> str:
    """Function that translates from English to Pig Latin.
    :param text: str - Text to translate.
    :return: str - Text translated to Pig Latin.
    """
    text = text.lower()
    if "xr" in text or "yt" in text:
        return f"{text}ay"

    if "ch" in text:
        text_splited = text.partition("ch")

    if "st" in text:
        text_splited = text.partition("st")
        return f"{''.join(text_splited[2:])}{''.join(text_splited[0:2])}ay"

    if "qu" in text:
        text_splited = text.partition("qu")
        for vowel in ["a", "e", "i", "o", "u"]:
            if vowel in text_splited[0]:
                return f"{text}ay"
        return f"{''.join(text_splited[2:])}{''.join(text_splited[0:2])}ay"

    # if "y" in text:
    #     text_splited = text.partition("y"):


print(translate("school"))
