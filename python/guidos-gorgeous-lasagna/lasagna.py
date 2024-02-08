"""
Preparing a lasagna.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time: int) -> int:
    """calculate the remaining lasagna time.

    Args:
        time (int): Baking time.

    Returns:
        int: Time remaining.
    """
    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(time: int) -> int:
    """Calculate the lasagna preparation time in minutes.

    Args:
        time (int): Preparation time.

    Returns:
        int: Preparation time in minutes.
    """
    return time * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int,
                            elapsed_bake_time: int) -> int:
    """Calculate elapsed time in minutes.

    Args:
        number_of_layers (int): Number of lasagna layer.
        elapsed_bake_time (int): Elapsed bake time.

    Returns:
        _type_: _description_
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
