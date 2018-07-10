#!/usr/bin/env python
""" Problem 3 daily-coding-problem.com """
import pickle 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.val

def serialize(tree: Node) -> str:
    if tree.left is None:
        left = "None"
    else:
        left = serialize(tree.left)

    if tree.right is None:
        right = "None"
    else:
        right = serialize(tree.right)

    s = (tree.val, left, right)
    return s

def deserialize(tree: tuple) -> Node:
    left = deserialize(tree[1]) if tree[1] != 'None' else None
    right = deserialize(tree[2]) if tree[2] != 'None' else None

    return Node(tree[0], left, right)

def serialize_easy(tree: Node ) -> str:
    return pickle.dumps(tree)
    
def deserialize_easy(tree: str) -> Node:
    return pickle.loads(tree)


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    assert deserialize(serialize(node)).left.left.val == 'left.left'    
    assert deserialize_easy(serialize_easy(node)).left.left.val == 'left.left'