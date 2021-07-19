from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def iter_list(l):
    while l is not None:
        yield l
        l=l.next

def reverse_sublist(s: ListNode, b: int, e: int) -> Optional[ListNode]:
    b-=1
    e-=1
    if s is None:
        return None
    stack=[]
    beg = s
    end=None
    for i, n in enumerate(iter_list(s)):
        if i<b:
            beg=n
        elif i>e:
            end = n
            break
        else:
            stack.append(n)

    while stack:
        beg.next=stack.pop()
        beg=beg.next
    beg.next=end
    return s

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
