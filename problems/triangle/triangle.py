from typing import List, Union


def is_valid(sides: List[Union[float,int]]) -> bool:
    [x, y, z] = sides
    return x > 0 and y > 0 and z > 0 and x + y > z


def equilateral(sides: List[Union[float,int]]) -> bool:
    sides.sort()
    return is_valid(sides) and sides.count(sides[0]) == 3


def isosceles(sides: List[Union[float,int]]) -> bool:
    sides.sort()
    return is_valid(sides) and sides[0] == sides[1] or sides[1] == sides[2]


def scalene(sides: List[Union[float,int]]) -> bool:
    sides.sort()
    return is_valid(sides) and sides[0] != sides[1] and sides[1] != sides[2]
