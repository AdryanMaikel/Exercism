def convert(number: int) -> str:
    """Function to check if the number is divisible by 3, 5, 7.
    :param number: int - Number to check.
    :return: str - String composed by "Pling", "Plang", "Plong" or the
    number.
    """
    result = []
    result.append("Pling") if number % 3 == 0 else None
    result.append("Plang") if number % 5 == 0 else None
    result.append("Plong") if number % 7 == 0 else None
    if len(result) == 0:
        return str(number)
    return "".join(result)
