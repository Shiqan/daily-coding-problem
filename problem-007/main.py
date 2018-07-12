#!/usr/bin/env python
""" Problem 7 daily-coding-problem.com """

import string
from typing import Dict, List


def decode(message: str, mapping:Dict[str, str]) -> int:
    if len(message) <= 1:
        return 1

    variants = 0
    for i in range(1, len(message)+1):
        head = message[:i]
        tail = message[i:]
        if head in mapping:
            variants += decode(tail, mapping)

    return variants


def decode_cache(message: str, mapping:Dict[str, str]) -> int:
    def _decode(message, mapping, cache):
        if len(message) <= 1:
            return 1

        if message in cache:
            return cache[message]
        
        variants = 0
        for i in range(1, len(message)+1):
            head = message[:i]
            tail = message[i:]
            if head in mapping:
                variants += _decode(tail, mapping, cache)

        cache[message] = variants
        return variants

    return _decode(message, mapping, {})


if __name__ == '__main__':
    mapping = {str(i+1):letter for i, letter in enumerate(string.ascii_lowercase)}


    message = '111'
    assert decode(message, mapping) == 3
    assert decode_cache(message, mapping) == 3
    
    message = '226'
    assert decode(message, mapping) == 3
    assert decode_cache(message, mapping) == 3

    message = '12131'
    assert decode(message, mapping) == 5
    assert decode_cache(message, mapping) == 5