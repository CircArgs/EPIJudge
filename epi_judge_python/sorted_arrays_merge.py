from typing import List
from functools import reduce
from test_framework import generic_test

# merge_sorted_arrays = lambda s: sorted(sum(s, []))

# def merge(a, b):
#     ret = []
#     while a and b:
#         if a[0] < b[0]:
#             ret.append(a[0])
#             a=a[1:]
#         else:
#             ret.append(b[0])
#             b=b[1:]
#     if a:
#         ret+=a
#     elif b:
#         ret+=b

#     return ret

# merge_sorted_arrays = lambda s: reduce(merge, s, [])


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    checked = [0] * len(sorted_arrays)
    ret = []
    done = 0
    while done < len(sorted_arrays):
        curr_i = 0
        curr_min = float("inf")
        done = 0
        for i in range(len(sorted_arrays)):
            c, a = checked[i], sorted_arrays[i]
            if c == len(a):
                done += 1
            elif curr_min > a[c]:
                curr_i = i
                curr_min = a[c]
        checked[curr_i] += 1
        ret.append(curr_min)

    return ret[:-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
