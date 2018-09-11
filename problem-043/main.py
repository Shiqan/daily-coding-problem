#!/usr/bin/env python
""" Problem 43 daily-coding-problem.com """

class Stack:
    def __init__(self):
        self.values = []
        self.max_values = []

    def push(self, val):
        self.values.append(val)
        current_max = self.max() if self.max_values else 0
        new_max = current_max if current_max > val else val
        self.max_values.append(new_max)
    
    def pop(self):
        self.values.pop()
        self.max_values.pop()

    def max(self):
        return self.max_values[-1]

    def __repr__(self):
        return self.values.__str__()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.max() == 3
    s.pop()
    assert s.max() == 2
    s.pop() 
    assert s.max() == 1