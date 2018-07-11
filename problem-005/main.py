#!/usr/bin/env python
""" Problem 5 daily-coding-problem.com """
from typing import Any

def cons(a: Any, b: Any) -> Any:
    def pair(f):
        return f(a, b)
    return pair

def car(f: Any) -> Any:
    return f(lambda a, b: a)

def cdr(f: Any) -> Any:
    return f(lambda a, b: b)

if __name__ == '__main__':
    p = cons(3, 4)
    assert car(p) == 3
    assert cdr(p) == 4

    a = cons(3, 4)
    b = cons(3, 4)
    c = cons(a, b)
    assert car(c) == a
    assert cdr(c) == b
