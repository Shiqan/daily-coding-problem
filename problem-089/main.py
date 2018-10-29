#!/usr/bin/env python
""" Problem 89 daily-coding-problem.com """


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return self.value

    def is_bst(self):
        if self is None:
            return True

        if self.left is None and self.right is None:
            return True

        if self.left != None and self.right is None:
            return self.value >= self.left.value and self.left.is_bst()
            
        elif self.right != None and self.left is None:
            return self.value <= self.right.value and self.right.is_bst()
        
        elif self.value < self.left.value and self.value > self.right.value:
            return False
        
        else:
            return self.left.is_bst() and self.right.is_bst()


if __name__ == "__main__":
    tree = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    assert tree.is_bst() == True

    tree = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, Node(14, Node(15))))
    assert tree.is_bst() == False