EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_time: int) -> int:
    '''
    :param elapsed_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(num_layers: int) -> int:
    '''
    Return total preparation time needed to complete number of layers of
    lasagna.
    '''
    return num_layers * 2


def elapsed_time_in_minutes(num_layers: int, elapsed_time: int) -> int:
    '''
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the
    time already spent baking and calculates the total elapsed minutes spent
    cooking the lasagna.
    '''
    return preparation_time_in_minutes(num_layers) + elapsed_time
