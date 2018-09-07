#!/usr/bin/env python
""" Problem 39 daily-coding-problem.com """

class GameOfLife:
    def __init__(self, cells=[], steps=5):
        self.cells = cells
        self.steps = steps

    def start(self):
        for _ in range(self.steps):
            print(self)
            self.next_tick()

    def next_tick(self):
        board = [
            # TODO
        ]
        self.cells = [i for i in board if self.is_alive_next_tick(i[0], i[1])]

    def is_alive_next_tick(self, x, y):
        return

    def __repr__(self):
        result = ""

        board = [
            # TODO
        ]
        for row in board:
            for i in row:
                result += "*" if i in self.cells else "."
            result += "\n"

        return result

if __name__ == "__main__":
    board = GameOfLife([(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 5)
    board.start()