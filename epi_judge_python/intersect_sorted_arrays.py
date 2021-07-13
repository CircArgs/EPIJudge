from typing import List

from test_framework import generic_test

def intersect_two_sorted_arrays(a, b):
    ai, bi = 0, 0
    ret = []
    while ai<len(a) and bi<len(b):
        # print(ai, bi)
        ea, eb = a[ai], b[bi]
        if ea == eb:
            if not ret or ea!=ret[-1]:
                ret.append(ea)
            ai+=1
            bi+=1
        elif ea<eb:
            ai+=1
        else:
            bi+=1
            
    return ret

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    return sorted(list(set(A).intersection(set(B))))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays,
        )
    )
