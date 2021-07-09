from typing import List
from itertools import chain
from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # n**2
    # max(chain((a-b for i, b in enumerate(prices) for a in prices[i+1:]), range(1)))
    curr_min = float("inf")
    curr_best = 0
    for i, p in enumerate(prices):
        curr_best = max(curr_best, p - curr_min)
        if curr_min > p:
            curr_min = p
    return curr_best


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
