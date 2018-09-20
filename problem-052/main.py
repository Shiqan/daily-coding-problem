#!/usr/bin/env python
""" Problem 52 daily-coding-problem.com """
from datetime import datetime

class Cache:
    def __init__(self, size):
        self.values = {}
        self.used = {}
        self.size = size

    def set(self, key, value):
        if len(self.values) >= self.size:
            rm = min(self.used, key=lambda k: self.used[k])
            del self.used[rm]
            del self.values[rm]
        
        self.values[key] = value
        self.used[key] = datetime.now()

        return (key, value)

    def get(self, key):
        if key in self.values:
            return self.values[key]
        return


if __name__ == "__main__":
    cache = Cache(5)
    for i in range(5):
        cache.set(i, i)
    
    cache.set(6, 6)
    assert cache.get(0) == None
    assert cache.get(6) != None
