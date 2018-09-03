#!/usr/bin/env python
""" Problem 35 daily-coding-problem.com """
from typing import List

def sortRGB(rgb: List[str]) -> List[str]:
    rgb.sort(reverse=True)
    return rgb

if __name__ == "__main__":
    assert sortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']