#!/usr/bin/env python
""" Problem 50 daily-coding-problem.com """

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return self.value


def evaluate(root: Node) -> int:
    left, right = "", ""
    if root.left is not None:
        left = evaluate(root.left)
    if root.right is not None:
        right = evaluate(root.right)
        
    return eval("({left}{value}{right})".format(left=left, value=root.value, right=right))
    
if __name__ == "__main__":
    tree = Node("*", Node("+", Node(3), Node(2)), Node("+", Node(4), Node(5)))
    assert evaluate(tree) == 45