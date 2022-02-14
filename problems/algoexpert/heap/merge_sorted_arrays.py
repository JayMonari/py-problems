from Heap import Heap  # type: ignore


def merge_sorted_arrays(arrays):
    sorted_list = []
    smallest_items = []
    for array_idx in range(len(arrays)):
        smallest_items.append(
            {"array_idx": array_idx, "element_idx": 0,  "num": arrays[array_idx][0]})
    min_heap = Heap(smallest_items)
    while not min_heap.is_empty():
        smallest_item = min_heap.remove()
        array_idx, element_idx, num = smallest_item["array_idx"], smallest_item["element_idx"], smallest_item["num"]
        sorted_list.append(num)
        if element_idx == len(arrays[array_idx]) - 1:
            continue
        min_heap.insert({"array_idx": array_idx, "element_idx": element_idx +
                        1, "num": arrays[array_idx][element_idx + 1]})
    return sorted_list


test = [
    [-92, -78, -68, 43, 46, 46, 79, 79],
    [-66, -49, -26, -16, 21, 28, 33, 50],
    [-40, -8, 12, 20, 36, 38, 81],
    [-76, -74, -62, -46, -23, 33, 42, 48, 55, 94]
]
print(merge_sorted_arrays(test))
