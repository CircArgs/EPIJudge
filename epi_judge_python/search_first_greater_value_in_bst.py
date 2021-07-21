from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

def find(t, v, c=BstNode(float('inf'))):
    if t is None:
        return c if c.data!=float('inf') else None
    if t.data>v and (c.data-v)>(t.data-v):
        c=t
    if t.data>v:
        return find(t.left, v,c)
    else:
        return find(t.right, v,c)


def find_first_greater_than_k(t, v, c=BstNode(float('inf'))) -> Optional[BstNode]:
    if t is None:
        return c if c.data!=float('inf') else None
    if t.data>v and (c.data-v)>(t.data-v):
        c=t
    if t.data>v:
        return find(t.left, v,c)
    else:
        return find(t.right, v,c)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_greater_value_in_bst.py",
            "search_first_greater_value_in_bst.tsv",
            find_first_greater_than_k_wrapper,
        )
    )
