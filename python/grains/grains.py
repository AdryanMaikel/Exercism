def square(number: int) -> int:
    """Calculate the total grains in each square of the chessboard.
    :param number: int - Chessboard house number.
    :return: int - Total of grains in chessboard house number.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    total_grains = 1
    if number == 1:
        return total_grains
    for _ in range(number-1):
        total_grains *= 2
    return total_grains


def total() -> int:
    """Calculate the total grains on the chessboard.
    :return: int - Total grains on the chessboard.
    """
    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
    return total_grains


print(total())
