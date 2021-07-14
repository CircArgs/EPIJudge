from typing import List

from test_framework import generic_test


def find_maximum_subarray(l: List[int]) -> int:
    if not l:
        return 0
    ms = [0, l[0]]
    ret = max(ms)
    for i in range(1, len(l)):
        ms[:] = ms[1], max(l[i], ms[1] + l[i])
        ret = max(ret, max(ms))
    return ret


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_sum_subarray.py", "max_sum_subarray.tsv", find_maximum_subarray
        )
    )
