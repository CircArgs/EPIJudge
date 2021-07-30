from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal(t):
    #the traversal return and the stack to emulate recursion
    ret, stack = [], [t]
    #indicator to tell us whether we have gone right and need to explore further lefts in the next iteration below
    #without this indicator, we will get stuck checking nodes for left positions we have already seen
    down = True
    #so long as there are left in the tree
    while stack:
        #get the top of the stack
        e = stack.pop()
        #we need to check lefts first
        if down:
            #indicates we have explored all leftmost positions
            down = False
            #if we have an element to the left add it to the stack 
            while e:
                stack.append(e)
                e = e.left
        #if we exhausted leftmost positions look to see if there is a right and if so we'll return the current position and\
        # (cont) add the right child to the stack while making sure we will check its left children
        else:
            ret.append(e.data)
            if e.right:
                #well need to go left more
                down = True
                stack.append(e.right)

    return ret
# def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
#     return inorder(tree)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_inorder.py", "tree_inorder.tsv", inorder_traversal
        )
    )
