from .data_structures.ListNode import ListNode


def reverse_list(head: ListNode) -> ListNode:
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node
