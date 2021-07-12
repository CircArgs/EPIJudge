from typing import List

from test_framework import generic_test

def bsearch(v, l, s=None, e=None):
    if len(l)<3:
        try:
            return 0, l.index(v)
        except ValueError:
            return False
    s=s if s is not None else 0
    
    e=e if e is not None else len(l)
    d=2
    lenl=e-s
    c = lenl//d+s
    m=c
    while (c>=s) and (c<e) and (l[c]!=v):
        d*=2
        mv = max(lenl//d, 1)
        if l[c]<v:
            t =c+ mv
        else:
            t =c- mv
        m = min(c, t)
        c=t
    return (c>=s) and (c<e) and (l[c]==v) and (m, c)

def lsearch(v, l):
    f = bsearch(v, l)
    c=-1
    while f and c:
        s, c = f
        if l[s]<v:
            f=bsearch(v, l, max(0, s), min(len(l), c))
        else:
            f=bsearch(v, l, 0, max(0, s))
    return c


def search_first_of_k(A: List[int], k: int) -> int:
    return lsearch(k, A)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )
