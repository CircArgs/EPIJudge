from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def preorder_traversal(t):
    if not t:
        return []
    ret = []
    stack = [t]
    while stack:
        e = stack.pop()
        ret.append(e.data)
        if e.right:
            stack.append(e.right)
        if e.left:
            stack.append(e.left)
    return ret



if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_preorder.py", "tree_preorder.tsv", preorder_traversal
        )
    )
