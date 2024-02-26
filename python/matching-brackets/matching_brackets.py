def is_paired(input_string: str) -> bool:
    """Check if this string contains valid {}[]() pair.

    :param input_string: str - String to be checked.
    :return: bool - Whether it contains valid pairs.
    """
    chars = "".join([char for char in input_string if char in "{}[]()"])
    for _ in range(2):
        for replace in ["{}", "[]", "()"]:
            while chars.__contains__(replace):
                chars = chars.replace(replace, "")
    if not chars:
        return True
    return False
