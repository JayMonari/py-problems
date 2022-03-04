from typing import Dict, List, Tuple


Inventory = Dict[str, int]
Items = List[str]


def create_inventory(items: Items) -> Inventory:
    '''
    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    '''
    return {it: items.count(it) for it in items}


def add_items(inventory: Inventory, items: Items) -> Inventory:
    '''
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    '''
    for it in set(items):
        inventory.update({it: (inventory.get(it) or 0) + items.count(it)})
    return inventory


def delete_items(inventory: Inventory, items: Items) -> Inventory:
    '''
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    '''
    return {it: (count - items.count(it) if count - items.count(it) > 0 else 0)
            for it, count in inventory.items()}


def list_inventory(inventory: Inventory) -> List[Tuple[str, int]]:
    '''
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    '''
    return [(it, count) for it, count in inventory.items() if count > 0]
