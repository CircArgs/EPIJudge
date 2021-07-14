from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(s: int, pts: List[int]) -> int:
    sols = [1, *([0] * s)]
    for p in pts:
        for i in range(p, s + 1):
            temp = i - p
            sols[i] += sols[temp]
    return sols[-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )
