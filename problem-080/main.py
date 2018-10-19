#!/usr/bin/env python
""" Problem 80 daily-coding-problem.com """


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __repr__(self):
        return self.value


def deepest_node(tree: Node) -> Node:
    def inorder_traversal(tree: Node, level: int) -> Node:
        level += 1
        left_level = right_level = 0
        left_node = right_node = Node(None)

        if tree.left is not None:
            left_node, left_level = inorder_traversal(tree.left, level)
        elif tree.right is not None:
            right_node, right_level = inorder_traversal(tree.right, level)
        else:
            return (tree, level)

        return (left_node, left_level) if left_level > right_level else (right_node, right_level)

    return inorder_traversal(tree, 0)[0]


if __name__ == "__main__":
    tree = Node('a', Node('b', Node('d'), Node('c')))
    assert deepest_node(tree) == Node('d')
