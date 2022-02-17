from typing import Optional


class ListNode:
    def __init__(self, value: int, _next=None):
        self.value = value
        self.next: Optional[ListNode] = _next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node: Optional[ListNode] = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node
