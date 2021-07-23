import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from typing import List, Set

class GraphVertex:
    def __init__(self) -> None:
        self.edges: List["GraphVertex"] = []
            
    def __hash__(self):
        return id(self)

def is_deadlocked_h(graph: List[GraphVertex], seen: Set[GraphVertex] = set()) -> bool:
    if not graph:
        return False
    if any(g in seen for g in graph):
        return True
    else:
        return any(is_deadlocked_h(g.edges, {*seen, g}) for g in graph)

def is_deadlocked(g):
    # import pandas as pd; pd.to_pickle(g, 'tt.pkl')
    return is_deadlocked_h(g)

@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError("Invalid num_nodes value")
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError("Invalid vertex index")
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "deadlock_detection.py", "deadlock_detection.tsv", is_deadlocked_wrapper
        )
    )
