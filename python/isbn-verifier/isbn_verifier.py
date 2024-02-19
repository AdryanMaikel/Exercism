def is_valid(isbn: str) -> bool:
    """Check if is a isbn valid.
    :param isbn: str - Isbn to valided.
    :return: bool - If is a valid isbn.
    """
    isbn = isbn.replace("-", "")
    if not isbn or (not isbn[-1].isdigit() and not isbn.endswith("X")):
        return False
    numbers = [int(char) if char.isdigit() else "ERROR" for char in isbn[:-1]]
    if "ERROR" in numbers:
        return False
    numbers.append(10 if isbn.endswith("X") else int(isbn[-1]))
    if len(numbers) != 10:
        return False
    return sum([numbers[i] * j
                for i, j in enumerate(range(10, 0, -1))]) % 11 == 0
