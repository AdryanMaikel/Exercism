"""
Calculate money exchanges.
"""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Exchange money based on quantity and exchange rate.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can
    receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate the money of resulting from the exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to
    exchange now.
    :return: float - amount left of your starting currency after
    exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate final value of bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return number_of_bills * denomination


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculate the number of bills.

    :param budget: float - the amount of money you are planning to
    exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget/denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Calculate leftover after exchanging into bills.

    :param budget: float - the amount of money you are planning to
    exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given
    the current denomination.
    """
    return budget % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int,
                       denomination: int) -> int:
    """Calculate value after exchange.

    :param budget: float - the amount of your money you are planning to
    exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    rate = exchange_rate + exchange_rate * (spread / 100)
    exchange = exchange_money(budget, rate)
    amount_bills = get_number_of_bills(exchange, denomination)
    value_of_bills = get_value_of_bills(denomination, amount_bills)
    return value_of_bills
