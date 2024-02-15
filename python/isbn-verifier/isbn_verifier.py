def is_valid(isbn: str) -> bool:
    """Check if is a isbn valid.
    :param isbn: str - Isbn to valided.
    :return: bool - If is a valid isbn.
    """
    isbn = isbn.replace("-", "")
    numbers = []
    for number in isbn:
        if number == "X":
            number = 10
        numbers.append(int(number))

    if len(numbers) != 10:
        return False

    return (numbers[0] * 10 + numbers[1] * 9 + numbers[2] * 8 + numbers[3] *
            7 + numbers[4] * 6 + numbers[5] * 5 + numbers[6] * 4 + numbers[7]
            * 3 + numbers[8] * 2 + numbers[9] * 1) % 11 == 0


print(is_valid("3-598-21507-X"))
