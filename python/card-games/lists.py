"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list[int] - first rounds played.
    :param rounds_2: list[int] - second set of rounds played.
    :return: list[int] - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list[int] - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]):
    """Return if an average is using (first + last index values ) OR
    ('middle' card) == calculated average.

    :param hand: list[int] - cards in hand.
    :return: bool - does one of the approximate averages equal the `true
    average`?
    """
    first, last, average = hand[0], hand[-1], sum(hand) / len(hand)
    return average in ((first + last) / 2, hand[len(hand) // 2])


def average_even_is_average_odd(hand: list[int]):
    """Return if the (average of even indexed card values) == (average
    of odd indexed card values).

    :param hand: list[int] - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    cards_even = list(hand[::2])
    cards_odd = list(hand[1::2])
    return sum(cards_odd) / len(cards_odd) == sum(cards_even) / len(cards_even)


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list[int] - cards in hand.
    :return: list[int] - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
