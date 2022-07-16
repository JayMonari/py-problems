from typing import Optional
from .data_structures.ListNode import ListNode


def delete_node(node: Optional[ListNode]) -> None:
    node.val = node.next.val
    node.next = node.next.next
