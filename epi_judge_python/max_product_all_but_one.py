from typing import List

from test_framework import generic_test

from functools import reduce
def find_biggest_n_minus_one_product(A: List[int]) -> int:
    tot=reduce(lambda x, y: max(x)*y, A)
    return max(tot/e for e in A)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_product_all_but_one.py",
            "max_product_all_but_one.tsv",
            find_biggest_n_minus_one_product,
        )
    )
