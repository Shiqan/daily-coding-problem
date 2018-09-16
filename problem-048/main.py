#!/usr/bin/env python
""" Problem 48 daily-coding-problem.com """
from typing import List


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value and self.right == other.right and self.left == other.left

    def __repr__(self):
        return self.value

def reconstruct(pre_order: List[str], in_order: List[str]) -> Node:
    root = Node(pre_order[0])

    index = in_order.index(root.value)
    left, right = in_order[:index], in_order[index+1:]

    if left:
        root.left = reconstruct([i for i in pre_order if i in left], left)
    if right:
        root.right = reconstruct([i for i in pre_order if i in right], right)

    return root

if __name__ == "__main__":
    assert reconstruct(["a", "b", "d", "e", "c", "f", "g"], ["d", "b", "e", "a", "f", "c", "g"]) == \
        Node("a", Node("b", Node("d"), Node("e")), Node("c", Node("f"), Node("g")))