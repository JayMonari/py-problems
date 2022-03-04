from typing import List, Set, Tuple
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(name: str,
                      ingredients: List[str]) -> Tuple[str, Set[str]]:
    '''
    :param name: str
    :param ingredients: list
    :return: tuple of (name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    '''
    return name, set(ingredients)


def check_drinks(name: str, ingredients: List[str]) -> str:
    '''
    :param name: str
    :param ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    '''
    category = " Mocktail" if ALCOHOLS.isdisjoint(ingredients) else " Cocktail"
    return name + category


def categorize_dish(name: str, ingredients: List[str]) -> str:
    '''
    :param name: str
    :param ingredients: list
    :return: str "dish name: CATEGORY"
    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    '''
    category = ""
    if VEGAN.issuperset(ingredients):
        category = "VEGAN"
    elif PALEO.issuperset(ingredients):
        category = "PALEO"
    elif KETO.issuperset(ingredients):
        category = "KETO"
    elif VEGETARIAN.issuperset(ingredients):
        category = "VEGETARIAN"
    elif OMNIVORE.issuperset(ingredients):
        category = "OMNIVORE"
    else:
        category = "ALIEN"

    return f"{name}: {category}"


Dish = Tuple[str, List[str]]
SpecialDish = Tuple[str, Set[str]]


def tag_special_ingredients(dish: Dish) -> SpecialDish:
    '''
    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `categories.py`.
    '''
    return dish[0], SPECIAL_INGREDIENTS.intersection(dish[1])


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    '''
    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    '''
    return set.union(*dishes)


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    '''
    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    '''
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: List[Set[str]],
                          intersection: Set[str]) -> Set[str]:
    '''
    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    '''
    singletons = (dish - intersection for dish in dishes)
    return set.union(*singletons)
