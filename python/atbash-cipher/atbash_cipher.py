PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "".join(reversed(PLAIN))


def encode(plain_text: str) -> str:
    encoding = ""
    count = 0
    for letter in plain_text.lower().replace(" ", "")\
            .replace(",", "").replace(".", ""):
        if count == 5:
            count = 0
            encoding += " "
        encoding += CIPHER[PLAIN.index(letter)]if letter.isalpha() else letter
        count += 1
    return encoding


def decode(ciphered_text: str) -> str:
    clean_text = ciphered_text.replace(" ", "").replace(".", "").replace(",", "")
    return "".join([PLAIN[CIPHER.index(letter)] if letter.isalpha() else letter
                    for letter in clean_text])
