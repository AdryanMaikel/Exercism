def is_paired(input_string):
    chars = "".join([char for char in input_string if char in "{}[]()"])
    for _ in range(2):
        for replace in ["{}", "[]", "()"]:
            while chars.__contains__(replace):
                chars = chars.replace(replace, "")
    if not chars:
        return True
    return False
