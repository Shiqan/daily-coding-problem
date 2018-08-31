#!/usr/bin/env python
""" Problem 32 daily-coding-problem.com """
from typing import List
from math import log

def arbitrage(table: List[List[int]]) -> bool:
    ''' see https://www.dailycodingproblem.com/blog/how-to-find-arbitrage-opportunities-in-python/ '''
    transformed_graph = [[-log(edge) for edge in row] for row in table]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False

if __name__ == "__main__":
    table = [
        [1, 2, 3], 
        [.5, 1, 1.33], 
        [1.5, .66, 1],
    ]
    assert arbitrage(table) == True
