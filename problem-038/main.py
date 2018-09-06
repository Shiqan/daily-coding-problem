#!/usr/bin/env python
""" Problem 38 daily-coding-problem.com """

def n_queens(n, board=[]):
    ''' see https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/'''
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += n_queens(n, board)
        board.pop()
    return count

def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]
    # Check if any queens can attack the last queen.
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True


if __name__ == "__main__":
    assert n_queens(1) == 1
    assert n_queens(4) == 2
    assert n_queens(7) == 40
    assert n_queens(10) == 724