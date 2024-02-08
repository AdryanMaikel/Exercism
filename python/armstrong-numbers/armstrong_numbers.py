def is_armstrong_number(number: int) -> bool:
    """Check to see if it is an armstrong number.
    :param number: int - Number to check.
    :return: bool - If it is an armstrong number.
    """
    str_number = str(number)
    len_number = len(str_number)
    armstrong_number = sum([pow(int(n), len_number) for n in str_number])
    return True if number.__eq__(armstrong_number) else False
