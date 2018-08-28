#!/usr/bin/env python
""" Problem 30 daily-coding-problem.com """
from typing import List


def water_trapped(elevation_map: List[int]) -> int:
    water = 0

    lw = elevation_map[0]
    lw_index = 0
    for rw_index, rw in enumerate(elevation_map[1:]):
        if lw <= rw:
            if rw_index+1 - lw_index > 1:
                water += sum(lw-i for i in elevation_map[lw_index+1:rw_index+1])
            lw = rw
            lw_index = rw_index
        
    if lw_index != rw_index:
        lw = max(elevation_map[rw_index:])
        water += water_trapped([lw] + elevation_map[rw_index:])

    return water

if __name__ == "__main__":
    assert water_trapped([2, 1, 2]) == 1
    assert water_trapped([3, 0, 1, 3, 0, 5]) == 8
    assert water_trapped([1, 5, 1, 4, 0, 5]) == 10
    assert water_trapped([1, 5, 0, 9, 0, 5]) == 10
    assert water_trapped([1, 5, 0, 0]) == 0
    assert water_trapped([3, 1, 5, 0, 0]) == 2