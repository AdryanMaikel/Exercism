"""
Check year is leap.
"""

from datetime import datetime, timedelta


def leap_year(year: int) -> bool:
    """Check if `year` is leap.
    :param year: int - Year to be checked.
    :return: bool - if is year leap.
    """
    one_day = timedelta(days=1)
    return (datetime(year, 2, 28) + one_day).day == 29
