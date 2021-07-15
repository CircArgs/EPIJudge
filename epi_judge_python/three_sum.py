from typing import List

from test_framework import generic_test


def has_three_sum(l: List[int], v: int) -> bool:
    l = set(l)
    for i in l:
        for j in l:
            if v - i - j in l:
                return True
    return False


if __name__ == "__main__":
    exit(generic_test.generic_test_main("three_sum.py", "three_sum.tsv", has_three_sum))
