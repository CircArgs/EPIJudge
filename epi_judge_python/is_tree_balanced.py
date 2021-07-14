from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def tree_height(n):
    return 1 + max(
        tree_height(n.left) if n.left else 0, tree_height(n.right) if n.right else 0
    )


def is_balanced(n):
    if not n:
        return True, 0
    left = is_balanced(n.left)
    if left[0]:
        right = is_balanced(n.right)
        if right[0]:
            return abs(right[1] - left[1]) < 2, max(left[1], right[1]) + 1
        else:
            return False, -1
    else:
        return False, -1


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return is_balanced(tree)[0]


if __name__ == "__main__":
    t = BinaryTreeNode(4)
    t.left = BinaryTreeNode(-4, None, BinaryTreeNode(7, None, BinaryTreeNode(6)))
    t.right = BinaryTreeNode(-2, BinaryTreeNode(1))
    print(t)
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
