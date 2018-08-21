#!/usr/bin/env python
""" Problem 23 daily-coding-problem.com """
from typing import List, Tuple


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.distance = None

    def set_parent(self, parent):
        self.parent = parent
        self.distance = parent.distance + 1


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.coord_matrix = [[Coord(i, j) for j in range(self.cols)] for i in range(self.rows)]

    def is_valid(self, coord: Tuple[int, int]) -> bool:
        return 0 <= coord[0] < self.rows and 0 <= coord[1] < self.cols

    def get_neighbours(self, coord: Coord) -> List[Coord]:
        x, y = coord.x, coord.y
        indexes = [(0,1), (0,-1), (1,0), (-1,0)]
        neighbours = []

        for i, j in indexes:
            if self.is_valid((x+i, y+j)):
                n = self.coord_matrix[x + i][y + j]
                if not self.matrix[x + i][y + j] and n.distance is None:
                    n.set_parent(coord)
                    neighbours.append(n)

        return neighbours

    def find_shortest_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> int:
        if not (self.is_valid(start) and self.is_valid(end)):
            return None

        start = self.coord_matrix[start[0]][start[1]]
        end = self.coord_matrix[end[0]][end[1]]
        wavefront = []

        start.distance = 0
        wavefront.append(start)

        while wavefront:
            current = wavefront[-1]
            if current is end:
                return end.distance

            neighbours = self.get_neighbours(current)
            if not neighbours:
                wavefront.pop()
            else:
                wavefront += neighbours

        return None

if __name__ == "__main__":
    matrix = Matrix([
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]
    ])
    
    assert matrix.find_shortest_path((3, 0), (0, 0)) == 7

    matrix = Matrix([
        [False, False,  False,  False, False],
        [True,  True,   True,  False, False],
        [False, False,  False,  False, True],
        [False, True,  True,  True, False],
        [False, False, False, False, False]
    ])
    
    assert matrix.find_shortest_path((3, 4), (0, 0)) == 15

    matrix = Matrix([
        []
    ])
    
    assert matrix.find_shortest_path((0, 0), (0, 0)) == None
