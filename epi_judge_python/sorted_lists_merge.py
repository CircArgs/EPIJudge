from typing import Optional
from copy import deepcopy
from list_node import ListNode, list_size
from test_framework import generic_test


def merge(l1, l2):
    base = l1 if l2.data > l1.data else l2
    ret = base
    c1, c2 = (l1, l2.next) if base == l2 else (l1.next, l2)

    while c1 and c2:
        base.next = c1 if c2.data > c1.data else c2
        c1, c2 = (c1, c2.next) if base.next == c2 else (c1.next, c2)
        base = base.next

    base.next = c1 or c2
    return ret


def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    if L1 is None and L2 is None:
        return None
    elif L1 is None:
        return L2
    elif L2 is None:
        return L1
    else:
        return merge(L1, L2)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
