import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook



def is_any_placement_feasible(m) -> bool:
    c = {}
    for i, j in m:
        if i in c:
            c[i].append(j)
        else:
            c[i] = [j]
    start =  i

    def bfs(s):
        curr = [(s, None)]
        tracker = {}
        i = 0
        while curr:
            next_curr = []
            for n, p in curr:
                if n not in tracker:
                    tracker[n] = i
                for e in c[n]:
                    if e == p:
                        continue
                    next_curr.append((e, n))
                    if e in tracker and (i - tracker[e]) % 2 == 1:
                        return False
            i += 1
            curr = next_curr
        return True

    return bfs(start)

@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    # if k <= 0:
    #     raise RuntimeError("Invalid k value")
    # graph = [GraphVertex() for _ in range(k)]

    # for (fr, to) in edges:
    #     if fr < 0 or fr >= k or to < 0 or to >= k:
    #         raise RuntimeError("Invalid vertex index")
    #     graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, edges))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_circuit_wirable.py",
            "is_circuit_wirable.tsv",
            is_any_placement_feasible_wrapper,
        )
    )
