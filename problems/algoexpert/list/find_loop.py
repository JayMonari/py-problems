
from typing import Optional


class ListNode:
    def __init__(self, value: int, _next=None):
        self.value: int = value
        self.next: Optional[ListNode] = _next


def find_loop(head: ListNode) -> Optional[ListNode]:
    if not head.next or not head.next.next:
        return head

    first = head.next
    second = head.next.next
    while first != second and first.next:
        first = first.next
        if second.next.next:
            second = second.next.next
    first = head
    while first != second and first.next and second.next:
        first = first.next
        second = second.next
    return first
