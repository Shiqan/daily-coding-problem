#!/usr/bin/env python
""" Problem 36 daily-coding-problem.com """

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return self.value

def find_second_largest(root: Node) -> int:
    parent = root.value

    while root.right:
        parent = root.value
        root = root.right

    return parent


if __name__ == "__main__":
    tree = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, Node(11), Node(14, Node(13), Node(15))))
    assert find_second_largest(tree) == 14

    tree = Node(27, Node(14, Node(10), Node(19)), Node(35, Node(31), Node(42)))
    assert find_second_largest(tree) == 35