#!/usr/bin/env python
""" Problem 93 daily-coding-problem.com """

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return self.value

    def __len__(self):
        left, right = 0, 0
        if self.left != None:
            left = len(self.left)
        if self.right != None:
            right = len(self.right)
        return 1 + left + right

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

def find_largest_bst(tree):
    if tree.is_bst():
        return tree
    elif tree.left != None and tree.left.is_bst():
        return find_largest_bst(tree.left)
    elif tree.right != None and tree.right.is_bst():
        return find_largest_bst(tree.right)
    
    return None


if __name__ == "__main__":
    tree = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
    assert find_largest_bst(tree) == tree

    tree = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, Node(14, Node(15))))
    assert find_largest_bst(tree) == tree.left