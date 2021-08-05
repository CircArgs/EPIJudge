from typing import List

from test_framework import generic_test, test_utils

from itertools import product
from functools import lru_cache

from itertools import product
from functools import lru_cache

@lru_cache(10)
def print_all_braces(n):
    if n == 0:
        return {""}
    ret = set()
    for i in range(1, n):
        a = print_all_braces(i)
        b = print_all_braces(n - i)
        ret=ret.union({f"{s}{t}" for s, t in product(a, b)})
    ret=ret.union({f"({s})" for s in print_all_braces(n - 1)})
    return ret
def generate_balanced_parentheses(n: int) -> List[str]:
    return list(print_all_braces(n))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_balanced_parentheses.py",
            "enumerate_balanced_parentheses.tsv",
            generate_balanced_parentheses,
            test_utils.unordered_compare,
        )
    )
