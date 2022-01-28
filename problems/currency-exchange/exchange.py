def estimate_value(budget: float, exchange_rate: float) -> float:
    '''
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return:
    '''
    return budget / exchange_rate


def get_change(budget: int, exchanging_value: int) -> float:
    '''
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return:
    '''
    return budget - exchanging_value


def get_value(denomination: int, number_of_bills: int) -> int:
    '''
    :param denomination: int - the value of a bill.
    :param number_of_bills: int amount of bills you received.
    :return:
    '''
    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    '''
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return:
    '''
    return int(budget / denomination)


def exchangeable_value(budget: float, exchange_rate: float, spread: int,
                       denomination: int) -> int:
    '''
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return:
    '''
    added_percent = exchange_rate * spread / 100
    total_rate = exchange_rate + added_percent
    estimate = estimate_value(budget, total_rate)
    num_bills = get_number_of_bills(estimate, denomination)
    return num_bills * denomination


def unexchangeable_value(budget: float, exchange_rate: float, spread: int,
                         denomination: int) -> int:
    added_percent = exchange_rate * spread / 100
    total_rate = exchange_rate + added_percent
    estimate = estimate_value(budget, total_rate)
    return int(estimate % denomination)
