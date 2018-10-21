#!/usr/bin/env python
""" Problem 81 daily-coding-problem.com """
from typing import Dict, List
import string
from itertools import product


def decode(message: int, mapping: Dict[int, List[str]]) -> List[str]:
    result = (list(mapping[int(letter)]) for letter in str(message))
    return ["".join(i) for i in product(*result)]


if __name__ == "__main__":
    mapping = {idx+1: string.ascii_lowercase[value:value+3] for idx, value in enumerate(range(0, len(string.ascii_lowercase), 3))}
    assert decode(12, mapping) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
