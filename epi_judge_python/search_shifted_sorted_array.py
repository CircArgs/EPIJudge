from typing import List

from test_framework import generic_test


def search_smallest(arr: List[int]) -> int:
    # from a case analysis we can see we can find the index of the minimum value (the rotation value)
    # by doing a binary search where at each step we see if the pivot is less than or greater than (array is distinct so no ==)
    # if the pivot is greater then we know the right half has the minimum
    # otherwise the left half does
    mn=None
    l=0
    h=len(arr)-1
    while (h-l)>1:
        pivot = l+(h-l)//2
        mn=min(((i, arr[i]) for i in (mn if mn else l, l, h, pivot)), key=lambda x: x[1])[0]
        if arr[pivot]>arr[h]:
            l=pivot+1
        else:
            h=pivot
    return min(((i, arr[i]) for i in (mn if mn else l, l, h)), key=lambda x: x[1])[0]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_shifted_sorted_array.py",
            "search_shifted_sorted_array.tsv",
            search_smallest,
        )
    )
