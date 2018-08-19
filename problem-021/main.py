#!/usr/bin/env python
""" Problem 21 daily-coding-problem.com """
from typing import List, Tuple


def rooms_required(times: List[Tuple[int, int]]) -> int:
    def _helper(times: List[Tuple[int, int]], count: int=0) -> int:
        if not times:
            return count

        times.sort()
        _, end = times[0]

        _temp = []
        for _, (start, new_end) in enumerate(times[1:]):
            if start < end:
                _temp.append((start, new_end))
            else:
                end = new_end
        
        count += 1
        return _helper(_temp, count)

    return _helper(times)

if __name__ == "__main__":
    assert  rooms_required([]) == 0
    assert  rooms_required([(30, 75), (0, 50), (60, 150)]) == 2
    assert  rooms_required([(30, 75), (40, 75), (75, 150), (0, 50), (60, 150), (150, 160), (50,60)]) == 3