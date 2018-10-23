#!/usr/bin/env python
""" Problem 83 daily-coding-problem.com """

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __eq__(self, other):
        if other is None:
            return self.value is None and self.left is None and self.right is None
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __repr__(self):
        return self.value

    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left != None:
            self.left.reverse()
        if self.right != None:
            self.right.reverse()



if __name__ == "__main__":
    tree = Node("a", Node("b", Node("d"), Node("e")), Node("c", Node("f")))
    reverse = Node("a", Node("c", None, Node("f")), Node("b", Node("e"), Node("d")))
    
    tree.reverse()
    assert tree == reverse

    tree.reverse()
    assert tree == tree