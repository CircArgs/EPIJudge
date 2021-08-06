import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple("Item", ("weight", "value"))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    def dfs(sack, weight, value):
#         print(sack, weight, value)
        mv, ms = value, sack
        for item in items:
            if (item not in sack) and ((item.weight+weight)<=capacity):
                temp = dfs({*sack, item}, item.weight+weight, value+item.value)
#                 print(temp)
                if temp[1]>mv:
                    mv=temp[1]
                    ms=temp[0]
        return ms, mv
#     import pdb; pdb.set_trace()
    return dfs(set(), 0, 0)[1]


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
