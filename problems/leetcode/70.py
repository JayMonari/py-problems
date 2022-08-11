def fib_stairs(steps: int) -> int:
    prev = 0
    curr = 1
    for _ in range(steps):
        next_ = prev + curr
        prev = curr
        curr = next_
    return curr
