#!/usr/bin/env python
""" Problem 88 daily-coding-problem.com """

def divide(a: int, b: int) -> int:
    result = 0
    while a >= b:  
        a -= b 
        result += 1
        
    return result

if __name__ == "__main__":
    assert divide(1, 2) == 0
    assert divide(8, 2) == 4
    assert divide(9, 2) == 4