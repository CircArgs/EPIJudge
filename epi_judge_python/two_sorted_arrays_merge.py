from typing import List

from test_framework import generic_test

# def merge(l1, l2):

#     l1[:]=l1[:curr]
def merge_two_sorted_arrays(l1: List[int], c: int, l2: List[int], _: int) -> None:
    l1.reverse()
    l1[-c:]=l1[-c:][::-1]
    curr=stopj=0
    for i in range(c):
        e1=l1[-(c-i)]
        for j in range(stopj, len(l2)):
            e2=l2[j]
            if e2<=e1:
                l1[curr]=e2
                curr+=1
            else:
                l1[curr]=e1
                l1[-(c-i)]=None
                curr+=1
                stopj=j
                break
    for j in range(stopj, len(l2)):
        e2=l2[j]
        l1[curr]=e2
        curr+=1
    # l1[:]=l1[:curr]
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "two_sorted_arrays_merge.py",
            "two_sorted_arrays_merge.tsv",
            merge_two_sorted_arrays_wrapper,
        )
    )
