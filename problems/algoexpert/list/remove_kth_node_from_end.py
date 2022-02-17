from typing import Optional


class ListNode:
    def __init__(self, value: int, _next=None):
        self.value: int = value
        self.next: Optional[ListNode] = _next


def remove_kth_node_from_end(head: Optional[ListNode], k: int) -> None:
    if not head:
        return
    counter: int = 1
    lead_node: Optional[ListNode] = head
    while counter <= k and lead_node:
        lead_node = lead_node.next
        counter += 1
    if lead_node is None and head.next:
        head.value = head.next.value
        head.next = head.next.next
        return

    before_kth_node = head
    while lead_node.next is not None:
        lead_node = lead_node.next
        before_kth_node = before_kth_node.next

    before_kth_node.next = before_kth_node.next.next
