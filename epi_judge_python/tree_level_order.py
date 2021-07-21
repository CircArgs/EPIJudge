from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(t: BinaryTreeNode):
    if not t:
        return []
    ret = [[t]]
    temp=True
    while temp:
        temp = []
        prev = []
        for n in ret[-1]:
            prev.append(n.data)
            if t.left or t.right:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
        ret[-1]=prev
        if temp:
            ret.append(temp)
                
                
    return ret


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_level_order.py", "tree_level_order.tsv", binary_tree_depth_order
        )
    )
