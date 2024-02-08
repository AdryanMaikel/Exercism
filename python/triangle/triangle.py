"""
Check triangle types.
"""


def equilateral(sides: list[int]) -> bool:
    """Check if the type of  triangle is equilateral.
    :param sides: list[int] - Sides of triangle.
    :return: bool - if is equilateral.
    """
    a, b, c = sides
    if (a > 0 and b > 0 and c > 0) and a == b == c:
        return True
    return False


def isosceles(sides: list[int]) -> bool:
    """Check if the type of  triangle is isosceles.
    :param sides: list[int] - Sides of triangle.
    :return: bool - if is isosceles.
    """
    a, b, c = sides
    if not (a > 0 and b > 0 and c > 0) or \
           (a + b <= c or a + c <= b or b + c <= a):
        return False
    if (a == b and a != c) or (b == c and c != a) or \
       (a == c and c != b) or (a == b and a == c):
        return True
    return False


def scalene(sides: list[int]) -> bool:
    """Check if the type of  triangle is scalene.
    :param sides: list[int] - Sides of triangle.
    :return: bool - if is scalene.
    """
    a, b, c = sides
    if not (a > 0 and b > 0 and c > 0) or \
           (a + b <= c or a + c <= b or b + c <= a):
        return False
    if a != b and a != c and b != c:
        return True
    return False
