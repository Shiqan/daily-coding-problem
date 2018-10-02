#!/usr/bin/env python
""" Problem 63 daily-coding-problem.com """
from typing import List

def is_word_in_matrix(word: str, matrix: List[List[str]]) -> bool:
    def _check_right(word: str, row: List[str]) -> bool:
        return word in "".join(row)
    
    def _check_down(word: str, i: int, matrix: List[List[str]]) -> bool:
        return word in "".join(row[i] for row in matrix)

    first_char = word[0]
    row_lenght = len(matrix[0])
    for row in range(len(matrix)):
        for col in range(row_lenght):
            if first_char == matrix[row][col]:
                return _check_right(word, matrix[row][col:]) or _check_down(word, col, matrix[row:])

    return False

if __name__ == "__main__":
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]
    assert is_word_in_matrix("FOAM", matrix) == True
    assert is_word_in_matrix("MASS", matrix) == True
    assert is_word_in_matrix("HELLO", matrix) == False
