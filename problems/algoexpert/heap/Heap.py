from typing import Callable, List


class Heap:
    def __init__(self,
                 comparison_function: Callable[[int, int], bool],
                 array: List[int]) -> None:
        self.comparison_function = comparison_function
        self.heap = self.__make_heap(array)

    def __len__(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def peek(self) -> int:
        return self.heap[0]

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.__sift_up(len(self.heap) - 1, self.heap)

    def remove(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        pop_val: int = self.heap.pop()
        self.__sift_down(0, len(self.heap) - 1, self.heap)
        return pop_val

    def __compare(self, idx1: int, idx2: int, heap: List[int]) -> bool:
        return self.comparison_function(heap[idx1], heap[idx2])

    def __make_heap(self, array: List[int]) -> List[int]:
        parent_idx1: int = len(array) - 2 // 2
        for idx in reversed(range(parent_idx1 + 1)):
            self.__sift_down(idx, len(array) - 1, array)
        return array

    def __sift_down(self, idx: int, end_idx: int, heap: List[int]) -> None:
        child1_idx: int = idx * 2 + 1
        while child1_idx <= end_idx:
            swap_idx: int = self.__get_swap_idx(idx, end_idx, heap)
            if not self.__compare(swap_idx, idx, heap):
                break
            heap[idx], heap[swap_idx] = heap[swap_idx], heap[idx]
            idx = swap_idx
            child1_idx = idx * 2 + 1

    def __get_swap_idx(self, idx: int, end_idx: int, heap: List[int]) -> int:
        child1_idx: int = idx * 2 + 1
        child2_idx: int = idx * 2 + 2
        if child2_idx <= end_idx:
            if self.__compare(child2_idx, child1_idx, heap):
                return child2_idx
            else:
                return child1_idx
        else:
            return child1_idx

    def __sift_up(self, idx: int, heap: List[int]) -> None:
        parent_idx: int = (idx - 1) // 2
        while idx > 0:
            if not self.__compare(idx, parent_idx, heap):
                break
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2


max_heap = Heap(lambda a, b: a > b, [1, 2, 3, 4, 5])
print(
    max_heap,
    max_heap.peek(),
    max_heap.remove(),
    max_heap.insert(1234),
    max_heap.peek()
)
min_heap = Heap(lambda a, b: a < b, [54, 3, 2, 1])
print(
    min_heap,
    min_heap.peek(),
    min_heap.remove(),
    min_heap.insert(-1234),
    min_heap.peek(),
)
