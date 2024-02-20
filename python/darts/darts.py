from math import sqrt


def score(x: float, y: float) -> int:
    """Function to calculate the score of a darts game.
    :param x: float - X position in target.
    :param y: float - Y position in target.
    :return: int - Score number.
    """
    distance = sqrt(x ** 2 + y ** 2)
    print(distance)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
