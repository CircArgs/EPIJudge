from typing import List

from test_framework import generic_test


from collections import namedtuple

Pos = namedtuple('Pos', ('x', 'y'))
moves=[(-1, 0), (1, 0), (0, 1), (0, -1)]
def fill_surrounded_regions(m) -> None:


    def can_move(p: Pos, x: int, y: int):
        new = Pos(p.x+x, p.y+y)
        if new.x>=0 and new.y>=0 and new.x<len(m[0]) and new.y<len(m) and m[new.y][new.x]=='W':
    #         m[new.y][new.x]=='B'
            return new
        else:
            return False

    

    def is_outside(p):
        return p.x == 0 or p.y == 0 or (p.x + 1) == len(m[0]) or (p.y + 1) == len(m)

    def can_reach_outside(p):
        level={p}
        while True:
            # print(level)
            next_level=set()
            for p in level:
                for move in moves:
                    new = can_move(p, *move)
                    if new and new not in level:
                        if is_outside(new):
                            return True
                        else:
                            next_level.add(new)
            # print('n', next_level)
            if not next_level:
                for p in level:
                    m[p.y][p.x]='B'
                return False
            level={*level, *next_level}


    def foo(m):
        for j in range(len(m[0])):
            for i in range(len(m)):
                p = Pos(j, i)
                # print(p)
                if m[i][j]=='W' and not is_outside(p):
                    can_reach_outside(p)
            
    foo(m)

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_enclosed_regions.py",
            "matrix_enclosed_regions.tsv",
            fill_surrounded_regions_wrapper,
        )
    )
