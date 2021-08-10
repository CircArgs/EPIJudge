import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple
from typing import List

Item = namedtuple("Item", ("weight", "value"))
Sack = namedtuple("Sack", ('items', "weight", "value"))

def foo(items, capacity):
    if capacity<0:
        return float('-inf')
    if len(items)==0 or capacity==0:
        return 0
    item=next(iter(items))
    return max(item.value+foo(items-{item}, capacity-item.weight), foo(items-{item}, capacity))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    cache = [[0] * (capacity + 1) for _ in range(2)]
    for item in items:
        for c in range(capacity + 1):
            wo = cache[0][c]
            w = c >= item.weight and cache[0][c - item.weight] + item.value
            cache[1][c] = max(w, wo)
        cache = [cache[-1], [0] * (capacity + 1)]
    return cache[0][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "knapsack.py", "knapsack.tsv", optimum_subject_to_capacity_wrapper
        )
    )
