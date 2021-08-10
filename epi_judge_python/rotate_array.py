import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(k: int, A: List[int]) -> None:
    k%=len(A)
    if k!=0:
        A[:k], A[k:] = A[-k:], A[:-k]


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "rotate_array.py", "rotate_array.tsv", rotate_array_wrapper
        )
    )
