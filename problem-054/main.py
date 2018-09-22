#!/usr/bin/env python
""" Problem 54 daily-coding-problem.com """
from typing import List, Tuple

def sudoku(board: List[List[int]]) -> List[List[int]]:
    if is_complete(board):
        return board

    row, col = find_empty_coord(board)
    # set r, c to a val from 1 to 9
    for i in range(1, 10):
        board[row][col] = i
        if is_valid(board):
            result = sudoku(board)
            if is_complete(result):
                return result
        board[row][col] = 0
    return board

def is_complete(board: List[List[int]]) -> bool:
    return all(all(val is not 0 for val in row) for row in board)

def find_empty_coord(board: List[List[int]]) -> Tuple[int, int]:
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
    return False

def is_valid(board: List[List[int]]) -> bool:
    def _is_rows_valid(board: List[List[int]]) -> bool:
        for row in board:
            if contain_duplicates(row):
                return False
        return True

    def _is_cols_valid(board: List[List[int]]) -> bool:
        row_lenght = len(board[0])
        for j in range(row_lenght):
            if contain_duplicates([board[i][j] for i in range(len(board))]):
                return False
        return True

    def _is_blocks_valid(board: List[List[int]]) -> bool:
        row_lenght = len(board[0])
        
        for i in range(0, row_lenght, 3):
            for j in range(0, row_lenght, 3):
                block = [board[i+k][j+l] for k in range(3) for l in range(3)]
                if contain_duplicates(block):
                    return False
        return True

    return _is_rows_valid(board) and _is_cols_valid(board) and _is_blocks_valid(board)

def contain_duplicates(arr: List[int]) -> bool:
    arr = [i for i in arr if i != 0]
    return len(arr) != len(set(arr))

if __name__ == "__main__":
    board = [
        [0,2,0, 5,0,1, 0,9,0],
        [8,0,0, 2,0,3, 0,0,6],
        [0,3,0, 0,6,0, 0,7,0],
        
        [0,0,1, 0,0,0, 6,0,0],
        [5,4,0, 0,0,0, 0,1,9],
        [0,0,2, 0,0,0, 7,0,0],

        [0,9,0, 0,3,0, 0,8,0],
        [2,0,0, 8,0,4, 0,0,7],
        [0,1,0, 9,0,7, 0,6,0],
    ]

    solved = [
        [4,2,6, 5,7,1, 3,9,8],
        [8,5,7, 2,9,3, 1,4,6],
        [1,3,9, 4,6,8, 2,7,5],
        
        [9,7,1, 3,8,5, 6,2,4],
        [5,4,3, 7,2,6, 8,1,9],
        [6,8,2, 1,4,9, 7,5,3],

        [7,9,4, 6,3,2, 5,8,1],
        [2,6,5, 8,1,4, 9,3,7],
        [3,1,8, 9,5,7, 4,6,2],
    ]

    assert sudoku(board) == solved