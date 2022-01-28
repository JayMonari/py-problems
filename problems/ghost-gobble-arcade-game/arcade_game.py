def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    '''
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    '''
    return True if power_pellet_active and touching_ghost else False


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    '''
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    '''
    return True if touching_power_pellet or touching_dot else False


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    '''
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    '''
    return True if not power_pellet_active and touching_ghost else False


def win(has_eaten_all_dots: bool, power_pellet_active: bool,
        touching_ghost: bool) -> bool:
    '''
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    '''
    if touching_ghost and not power_pellet_active:
        return False
    return True if has_eaten_all_dots else False
