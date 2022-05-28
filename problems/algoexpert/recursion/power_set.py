def main() -> None:
    sum = 0
    for s in powerset([n for n in range(1, 27)]):
        for v in s:
            sum += v
    print(sum)


def powerset(nums: list[int]) -> list[list[int]]:
    subsets: list[list[int]] = [[]]
    index = 0
    while index < 2**len(nums):
        subset: list[int] = []
        for i, num in enumerate(nums):
            if index & (1 << i) > 0:
                subset.append(num)
        subsets.append(subset)
        index += 1
    return subsets


if __name__ == "__main__":
    main()
