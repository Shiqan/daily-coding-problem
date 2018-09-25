#!/usr/bin/env python
""" Problem 57 daily-coding-problem.com """
from typing import List

def break_text(s: str, k: int) -> List[str]:
    arr = s.split(" ")
    result = []

    _tmp, arr = arr[0], arr[1:]
    
    while arr:
        new_temp = _tmp + " " + arr[0]
        if len(new_temp) <= k:
            _tmp = new_temp
        else:
            result.append(_tmp)
            _tmp = arr[0]
        arr = arr[1:]
    result.append(_tmp)

    return result

if __name__ == "__main__":
    assert break_text("the quick brown fox jumps over the lazy dog", 10) == ["the quick", "brown fox", "jumps over", "the lazy", "dog"]