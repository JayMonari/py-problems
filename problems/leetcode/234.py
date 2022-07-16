from .data_structures.ListNode import ListNode


def is_palindrome_list(head: ListNode) -> bool:
    vals: list[int] = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]
