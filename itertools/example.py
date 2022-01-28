import itertools
from typing import Iterable

letters = ['a', 'b', 'c', 'd']
nums = [0, 1, 2, 3]
names = ["Jay", "Aleksander"]

for item in itertools.combinations(letters, 2):
    print(item)

for item in itertools.permutations(letters, 2):
    print(item)

# Quick repr for conversion between decimal, binary, and hex.
for n in itertools.product("01", repeat=8):
    n = "".join(n)
    print(f"DEC: {int(n, 2)}, BIN: {n}, HEX: {hex(int(n, 2))}")

for item in itertools.chain(letters, nums, names):
    print(item)

# One line infinite counter
counter = itertools.count(start=5, step=-2.5)

next(counter)
next(counter)
next(counter)

daily_data = list(zip(itertools.count(), [100, 200, 300, 400]))

print(daily_data)

# Want a zip for the longest?
daily_data2 = list(itertools.zip_longest(range(10), [100, 200, 300, 400]))

cycle: Iterable[str] = itertools.cycle(("On", "Off"))

print(next(cycle))
print(next(cycle))
print(next(cycle))

# Fancy python
sqaures = map(pow, range(10), itertools.repeat(2))

print(list(sqaures))

# Need any amount? Seeing stars *o*
sqaures = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)])

print(list(map(hex, [255, 20, 74])))

with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)
    for line in header:
        print(line, end='')

