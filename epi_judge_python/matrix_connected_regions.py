from typing import List

from test_framework import generic_test

from collections import namedtuple

Coord = namedtuple("Coord", ("x", "y"))



def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    c = Coord(x, y)

    base = image[c.x][c.y]

    def helper(c: Coord):
        # print(c)
        if (
            c.x < 0
            or c.x >= len(image[0])
            or c.y < 0
            or c.y >= len(image)
            or image[c.x][c.y] != base
        ):
            return
        image[c.x][c.y] = 1 - base
        for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            helper(Coord(c.x + i, c.y + j))
    helper(c)

def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "matrix_connected_regions.py", "painting.tsv", flip_color_wrapper
        )
    )
