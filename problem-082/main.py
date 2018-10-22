#!/usr/bin/env python
""" Problem 82 daily-coding-problem.com """

def read7(s: str, offset: int) -> str:
    return s[offset:offset+7]

def readN(s: str) -> str:
    result = []
    offset = 0
    while True:
        found = read7(s, offset)
        result.append(found)
        if not found:
            return result
        offset += 7

if __name__ == "__main__":
    result = readN("Hello world")
    assert result == ["Hello w", "orld", ""]