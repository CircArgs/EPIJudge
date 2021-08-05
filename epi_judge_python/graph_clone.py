import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List["GraphVertex"] = []

Node=GraphVertex

# idea is to follow tried and true create a dictionary tracking ids first pass
# unpack dictionary into graph second pass
def clone_graph(root):
    graph_dict={}
    def dfs(n):
        graph_dict[id(n)]=(GraphVertex(n.label), n)
        for n in n.edges:
            if id(n) not in graph_dict:
                dfs(n)
    dfs(root)
    for copy_node, node in graph_dict.values():
        copy_node.edges=[graph_dict[id(i)][0] for i in node.edges]
    return graph_dict[id(root)][0]

# def clone_graph(graph: GraphVertex) -> GraphVertex:
#     # TODO - you fill in here.
#     return GraphVertex(0)


def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure("Graph was not copied")

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure("Invalid vertex label")
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure("Edges mismatch")
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError("Invalid k value")
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError("Invalid vertex index")
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "graph_clone.py", "graph_clone.tsv", clone_graph_test
        )
    )
