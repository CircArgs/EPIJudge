from test_framework import generic_test

from collections import namedtuple
from typing import Union
from functools import lru_cache


Coord = namedtuple('Coord', ('x', 'y'))

moves=[Coord(0, 1), Coord(1, 0)]

def number_of_ways(n: int, m: int) -> int:
    def can_move(c: Coord, move: Coord)->Union[bool, Coord]:
        new=Coord(c.x+move.x, c.y+move.y)
        if new.x>=0 and new.y>=0 and new.x<n and new.y<m:
            return new
        return False
    @lru_cache(50)
    def foo(c: Coord):
        if c==Coord(n-1, m-1):
            return 1
        ret=0
        for move in moves:
            new=can_move(c, move)
            if new:
                ret+=foo(new)
        return ret
    return foo(Coord(0, 0))

from scipy.special import comb
def number_of_ways(n, m):
    return comb(n+m-2, n-1, exact=True)

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_traversals_matrix.py",
            "number_of_traversals_matrix.tsv",
            number_of_ways,
        )
    )
