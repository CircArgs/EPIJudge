import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple("Coordinate", ("x", "y"))

from functools import lru_cache

# def search(m, s, e):
#     if s == e:
#         return True
#     paths = []
#     for move in pots:
#         m_new, after = can_move(m, s, *move)
#         if after is not None:
#             paths.append(search(m_new, after, e))
#     return any(paths)




def search_maze(
    m: List[List[int]], s: Coordinate, e: Coordinate
) -> List[Coordinate]:
    @lru_cache(128)
    def can_move(n, x=0, y=0):
        new = Coordinate(n.x - x, n.y - y)
        if new.x < 0 or new.y < 0 or new.x >= len(m) or new.y >= len(m[0]) or m[new.x][new.y]==1:
            return None
        return new


    pots = [
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 0),
    ]


    def search(s, e, visited=set()):
        #     import pdb

        #     pdb.set_trace()
        if s == e:
            return [e]
        path = [s]
        for move in pots:
            after = can_move(s, *move)
            if after is not None and after not in visited:
                future = search(after, e, {*visited, after})
                if future and future[-1] == e:
                    path += future
                    return path
        return []
    return search(s, e)





























def path_element_is_feasible(maze, prev, cur):
    if not (
        (0 <= cur.x < len(maze))
        and (0 <= cur.y < len(maze[cur.x]))
        and maze[cur.x][cur.y] == WHITE
    ):
        return False
    return (
        cur == (prev.x + 1, prev.y)
        or cur == (prev.x - 1, prev.y)
        or cur == (prev.x, prev.y + 1)
        or cur == (prev.x, prev.y - 1)
    )


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_maze.py", "search_maze.tsv", search_maze_wrapper
        )
    )
