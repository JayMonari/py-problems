from typing import Optional
from .data_structures.ListNode import ListNode


def get_intersection_node(l1: ListNode, l2: ListNode) -> Optional[ListNode]:
    if not l1 or not l2:
        return None

    n1: ListNode = l1
    n2: ListNode = l2
    while n1 != n2:
        n1 = n1.next if n1 else l2
        n2 = n2.next if n2 else l1
    return n1
