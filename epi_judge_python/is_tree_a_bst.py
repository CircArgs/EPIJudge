from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(t):
    if not t:
        return []
    else:
        return (
            (inorder_traversal(t.left) if t.left else [])
            + [t.data]
            + (inorder_traversal(t.right) if t.right else [])
        )


def is_sorted(l):
    b = float("-inf")
    for i in l:
        if i >= b:
            b = i
        else:
            return False
    return True


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_sorted(inorder_traversal(tree))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst
        )
    )
