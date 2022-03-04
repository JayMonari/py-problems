def score(x: float, y: float) -> int:
    point = x*x + y*y
    if point <= 1:
        return 10
    elif point <= 25:
        return 5
    elif point <= 100:
        return 1

    return 0
