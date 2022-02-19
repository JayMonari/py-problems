def calculate_fib(number: int) -> int:
    if number == 0:
        return 0

    prev = 0
    curr = 1
    for _ in range(1, number):
        next = prev + curr
        prev = curr
        curr = next
    return curr


print(
    calculate_fib(1),
    calculate_fib(2),
    calculate_fib(3),
    calculate_fib(4),
    calculate_fib(5),
    calculate_fib(6),
    calculate_fib(7),
    calculate_fib(8),
    calculate_fib(9),
    calculate_fib(10),
    calculate_fib(11),
)
