COLOR_BANDS = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
               "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def value(colors: list[str]) -> int:
    return int("".join([str(COLOR_BANDS[color]) for color in colors[:2]]))
