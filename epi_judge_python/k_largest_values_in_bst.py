from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

class PoException(Exception):
    pass


def find_k_largest_in_bst(t: BstNode, k: int) -> List[int]:
   
    ret=[]

    def po(t):
        if t is None:
            return
        else:
            if t.right:
                po(t.right)
            if len(ret)>=k:
                raise PoException
            ret.append(t.data)
                
            if t.left:
                po(t.left)
    try:
        po(t)
    except PoException:
        pass
    return ret



if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py",
            "k_largest_values_in_bst.tsv",
            find_k_largest_in_bst,
            test_utils.unordered_compare,
        )
    )
