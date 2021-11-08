from functools import reduce
from typing import List


def get_rounds(number: int) -> List[int]:
    '''
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    '''
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    '''
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    '''
    return [*rounds_1, *rounds_2]


def list_contains_round(rounds: List[int], number: int) -> bool:
    '''
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    '''
    return number in rounds


def card_average(hand: List[int]) -> float:
    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    '''
    :param hand: list - cards in hand.
    :return: int - approximate average value of the cards in the hand.
    '''
    avg = card_average(hand)
    return avg in [(hand[0] + hand[-1]) // 2, hand[len(hand)//2]]


def average_even_is_average_odd(hand: List[int]) -> bool:
    '''
    :param hand: list - cards in hand.
    :return: int - approximate average value of the cards in the hand.
    '''
    evens = [n for n in hand if n % 2 == 0]
    odds = [n for n in hand if n % 2 == 1]

    return card_average(evens) == card_average(odds)


def maybe_double_last(hand: List[int]) -> List[int]:
    '''
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    '''
    hand[-1] = hand[-1] * 2 if hand[-1] == 11 else hand[-1]
    return hand
