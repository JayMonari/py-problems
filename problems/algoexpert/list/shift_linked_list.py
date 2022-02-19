from typing import Optional


class ListNode:
    def __init__(self, value: int, _next=None):
        self.value: int = value
        self.next: Optional[ListNode] = _next


def shift_linked_list(
        head: Optional[ListNode],
        k: int) -> Optional[ListNode]:
    list_length: int = 1
    list_tail: Optional[ListNode] = head
    while list_tail.next is not None:
        list_tail = list_tail.next
        list_length += 1

    offset: int = abs(k) % list_length
    if offset == 0:
        return head
    new_tail_position: int = list_length - offset if k > 0 else offset
    new_tail: Optional[ListNode] = head
    for _ in range(1, new_tail_position):
        new_tail = new_tail.next
    new_head: Optional[ListNode] = new_tail.next
    new_tail.next = None
    list_tail.next = head
    return new_head
