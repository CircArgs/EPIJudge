import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

def find_kth_node_binary_tree(t, k):
    # the traversal return and the stack to emulate recursion
    count, stack = 0, [t]
    # indicator to tell us whether we have gone right and need to explore further lefts in the next iteration below
    # without this indicator, we will get stuck checking nodes for left positions we have already seen
    down = True
    # so long as there are left in the tree
    while stack:
        # get the top of the stack
        e = stack.pop()
        # we need to check lefts first
        if down:
            # indicates we have explored all leftmost positions
            down = False
            # if we have an element to the left add it to the stack
            while e:
                stack.append(e)
                e = e.left
        # if we exhausted leftmost positions look to see if there is a right and if so we'll return the current position and\
        # (cont) add the right child to the stack while making sure we will check its left children
        else:
            count += 1
            if count == k:
                return e
            if e.right:
                # well need to go left more
                down = True
                stack.append(e.right)
    return

# def find_kth_node_binary_tree(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
#     # TODO - you fill in here.
#     return None


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_node_in_tree.py",
            "kth_node_in_tree.tsv",
            find_kth_node_binary_tree_wrapper,
        )
    )
