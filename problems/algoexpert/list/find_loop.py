
from typing import Optional


class ListNode:
    def __init__(self, value: int, _next=None):
        self.value: int = value
        self.next: Optional[ListNode] = _next


def find_loop(head: ListNode) -> Optional[ListNode]:
    if not head.next or not head.next.next:
        return head

    first: ListNode = head.next
    second: ListNode = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
