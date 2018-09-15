#!/usr/bin/env python
""" Problem 47 daily-coding-problem.com """
from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0

    for i, v in enumerate(prices):
        profit = max(profit, (max(prices[i:]) - v))

    return profit

def max_profit_reversed(prices: List[int]) -> int:
    profit = 0
    cache = 0

    for i in range(len(prices)-1, -1, -1):
        cache = max(cache, prices[i])
        profit = max(profit, cache-prices[i])
    
    return profit

if __name__ == "__main__":
    assert max_profit([9, 11, 8, 5, 7, 10]) == 5
    assert max_profit_reversed([9, 11, 8, 5, 7, 10]) == 5

    assert max_profit([9, 11, 8, 1, 2, 3, 5, 11]) == 10
    assert max_profit_reversed([9, 11, 8, 1, 2, 3, 5, 11]) == 10

    assert max_profit_reversed([5, 4, 3, 2, 1]) == 0
    assert max_profit_reversed([5, 4, 3, 2, 1]) == 0