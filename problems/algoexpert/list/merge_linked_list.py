from typing import Optional


class ListNode:
    def __init__(self, value: int, _next=None):
        self.value = value
        self.next: Optional[ListNode] = _next


def merge_lists(l1: Optional[ListNode],
                l2: Optional[ListNode]) -> Optional[ListNode]:
    sentinel: ListNode = ListNode(0)
    curr_node: ListNode = sentinel
    while (l1 and l2):
        if l1.value < l2.value:
            curr_node.next = l1
            l1 = l1.next
        else:
            curr_node.next = l2
            l2 = l2.next
        curr_node = curr_node.next
    curr_node.next = l1 if l1 else l2
    return sentinel.next
