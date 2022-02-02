from typing import List


# A disk has three values [length, width, height]
Disk = List[int]


def stack_disks(disks: List[Disk]) -> List[Disk]:
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [-1 for _ in disks]
    max_height_idx: int = 0
    for i, disk1 in enumerate(disks[1:], start=1):
        for j, disk2 in enumerate(disks[:i]):
            if not fits_on(disk1, disk2):
                continue

            height1 = disk1[2]
            if heights[i] < heights[j] + height1:
                heights[i] = height1 + heights[j]
                sequences[i] = j
            if heights[i] >= heights[max_height_idx]:
                max_height_idx = i
    return build_sequence(disks, sequences, max_height_idx)


def build_sequence(disks: List[Disk],
                   sequences: List[int],
                   curr_idx: int) -> List[Disk]:
    sequence: List[Disk] = []
    while curr_idx != -1:
        sequence.append(disks[curr_idx])
        curr_idx = sequences[curr_idx]
    return list(reversed(sequence))


def fits_on(c: Disk, o: Disk) -> bool:
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


test1 = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
test2 = [
    [3, 3, 4],
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [5, 5, 6],
    [1, 2, 1],
    [4, 4, 5],
    [1, 1, 4],
    [2, 2, 3]
]

print(stack_disks(test2), stack_disks(test1))
