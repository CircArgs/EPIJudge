from typing import List

from test_framework import generic_test, test_utils

def wrapper(l, k):
    l=set(l)
    ret=set()
    def size_k_subsets(s):
        if len(s)==k:
            ret.add(tuple(s))
        for i in l-s:
            size_k_subsets({*s, i})
    size_k_subsets(set())
    return ret

def wrapper(l, k):
    l=set(l)
    ret=[]
    ret_s=set()
    def size_k_subsets(s):
        if len(s)==k:
            temp=tuple(s)
            if temp not in ret_s:
                ret.append(list(temp))
                ret_s.add(temp)
            return
        for e in s:
            size_k_subsets(s-{e})
    size_k_subsets(l)
    return ret

def combinations(n: int, k: int) -> List[List[int]]:
    if k==0 or n==0:
        return [[]]
    curr=[{e} for e in range(1, n+1)]
    stop=False
    while not stop:
        temp=[]
        for i, e in enumerate(curr):
            for e2 in curr[i+1:]:
                t={*e, *e2}
                if len(t)==k:
                    stop=True
                temp.append(t)
        curr=temp

        
    return [list(e) for e in curr]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            "combinations.tsv",
            combinations,
            comparator=test_utils.unordered_compare,
        )
    )
