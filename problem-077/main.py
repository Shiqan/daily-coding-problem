#!/usr/bin/env python
""" Problem 77 daily-coding-problem.com """
from typing import List, Tuple
from collections import namedtuple


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    copy_intervals = intervals.copy()
    intervals.sort()
    remove_intervals = []
    Interval = namedtuple("Interval", ["start", "end"])

    current = Interval(start=intervals[0][0], end=intervals[0][1])
    for interval in intervals[1:]:
        i = Interval(start=interval[0], end=interval[1])
        if current.start < i.start and current.end > i.end:
            remove_intervals.append(interval)

        if current.start < i.start and current.end < i.end:
            current = i

    return [i for i in copy_intervals if i not in remove_intervals]


if __name__ == "__main__":
    assert merge_intervals([(1, 2), (2, 3), (0, 100)]) == [(0, 100)]
    assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
