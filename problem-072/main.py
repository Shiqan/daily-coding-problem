#!/usr/bin/env python
""" Problem 72 daily-coding-problem.com """
from typing import List, Tuple, Dict
from collections import Counter

def find_largest_value_path(graph: str, edges: List[Tuple[int, int]]) -> int:
    def walk_path(start: int, current_path: List[int], graph: str, edges_dict: Dict[int, List[int]]) -> int:
        current_path.append(start)
        walk_to = edges_dict.get(start, [])

        if not walk_to:
            return Counter(graph[i] for i in current_path).most_common()[0][1]

        if len(walk_to) == 1 and walk_to[0] == start:
            return 0

        max_value = 0
        for src in walk_to:
            result = walk_path(src, current_path, graph, edges_dict)
            max_value = result if result > max_value else max_value
            current_path = [start]

        return max_value

    edges_dict = {}
    for e in edges:
        edges_dict.setdefault(e[0], []).append(e[1])
        
    max_value = 0
    for e in edges_dict:
        result = walk_path(e, [], graph, edges_dict)
        max_value = result if result > max_value else max_value

    return max_value

if __name__ == "__main__":
    assert find_largest_value_path("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]) == 3
    assert find_largest_value_path("A", [(0, 0)]) == 0
