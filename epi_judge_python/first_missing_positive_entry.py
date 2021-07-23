from typing import List

from test_framework import generic_test


def find_first_missing_positive(A: List[int]) -> int:
    if not A:
        return 1
    upper=max(max(A), 0)
    A=set(A)
    for i in range(1, upper+2):
        if i not in A:
            return i


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "first_missing_positive_entry.py",
            "first_missing_positive_entry.tsv",
            find_first_missing_positive,
        )
    )
