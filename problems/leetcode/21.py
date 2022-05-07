from .data_structures.ListNode import ListNode


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    sentinel = ListNode(0)
    curr_node = sentinel
    while l1 and l2:
        if l1.val < l2.val:
            curr_node.next = l1
            l1 = l1.next
        else:
            curr_node.next = l2
            l2 = l2.next
        curr_node = curr_node.next
    curr_node.next = l1 if l1 else l2
    return sentinel.next
