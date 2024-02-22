"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one: list[int], list_two: list[int]) -> str:
    """Given any two lists A and B, determine if:

    * List A is equal to list B; or
    * List A contains list B (A is a superlist of B); or
    * List A is contained by list B (A is a sublist of B); or
    * None of the above is true, thus lists A and B are unequal

    :param list_one: list[int] - List one to compare.
    :param list_two: list[int] - List two to compare.
    :return: str - Comparation result.
    """
    if list_one == list_two:
        return EQUAL

    str_list_one = ",".join([str(n) for n in list_one])
    str_list_two = ",".join([str(n) for n in list_two])
    len_list_one = len(list_one)
    len_list_two = len(list_two)

    if len_list_one > len_list_two:
        if str_list_two in str_list_one:
            return SUPERLIST

    if len_list_two > len_list_one:
        if str_list_one in str_list_two:
            return SUBLIST

    return UNEQUAL
