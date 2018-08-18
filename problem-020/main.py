#!/usr/bin/env python
""" Problem 20 daily-coding-problem.com """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return " -> ".join([str(i.value) for i in self])

    def __iter__(self):
        cur = self
        while cur is not None:
            yield cur
            cur = cur.next


def find_intersection(left: Node, right: Node) -> int:
    visited = set(left)
    for cur_right in right:
        if cur_right in visited:
            return cur_right.value
    return None

if __name__ == "__main__":
    x = Node(8, Node(10))
    a = Node(3, Node(7, x))
    b = Node(99, Node(1, x))

    assert find_intersection(a, b) == 8
