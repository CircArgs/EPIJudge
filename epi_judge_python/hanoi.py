import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

cache={0:[], 1: [[0, 1]], 2: [[0,2],[0,1],[2,1]]}

swap=lambda x, a, b: x if x not in (a, b) else (a if x==b else b)
def adjust_indices(l: List[List[int]], a, b):

    return [ [swap(i, a, b), swap(j, a, b)] for i,j in l]

def compute_tower_hanoi_recursive(num_rings: int) -> List[List[int]]:
    if num_rings in cache:
        return cache[num_rings]
    else:
        # step1
        n_minus_1_sol=compute_tower_hanoi_recursive(num_rings-1)
        # step2
        base=adjust_indices(n_minus_1_sol, 1, 2)
        #step3
        base.append([0, 1])
        #step4
        base+=adjust_indices(n_minus_1_sol, 0, 2)

        return base

def compute_tower_hanoi_not_recursive(num_rings: int) -> List[List[int]]:
    if num_rings in cache:
        return cache[num_rings]
    else:
        n_minus_1_sol=cache[2]
        base=None
        for n in range(2, num_rings):
            # step2
            base=adjust_indices(n_minus_1_sol, 1, 2)
            #step3
            base.append([0, 1])
            #step4
            base+=adjust_indices(n_minus_1_sol, 0, 2)
            n_minus_1_sol=base
        return base

compute_tower_hanoi=compute_tower_hanoi_recursive

@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure(
                "Illegal move from {} to {}".format(
                    pegs[from_peg][-1], pegs[to_peg][-1]
                )
            )
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "hanoi.py", "hanoi.tsv", compute_tower_hanoi_wrapper
        )
    )
