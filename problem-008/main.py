#!/usr/bin/env python
""" Problem 8 daily-coding-problem.com """

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return self.value

def count_unival_subtrees(root: Node) -> int:
    def _is_unival(root):
        return _unival_helper(root, root.value)

    def _unival_helper(root, value):
        if root is None:
            return True
        if root.value == value:
            return _unival_helper(root.left, value) and _unival_helper(root.right, value)
        return False

    if root is None:
        return 0
    
    root_count = 1 if _is_unival(root) else 0
    left_count = count_unival_subtrees(root.left)
    right_count = count_unival_subtrees(root.right)

    return root_count + left_count + right_count

def count_unival_subtrees_cache(root: Node) -> int:
    def _count(root):
        if root is None:
            return 0, True
            
        left_count, is_left_unival = _count(root.left)
        right_count, is_right_unival = _count(root.right)
        total_count = left_count + right_count
        if is_left_unival and is_right_unival:
            if root.left is not None and root.value != root.left.value:
                return total_count, False
            if root.right is not None and root.value != root.right.value:
                return total_count, False
            return total_count + 1, True
        return total_count, False

    count, _ = _count(root)
    return count


        
if __name__ == '__main__':
    tree = Node(0, Node(1), Node(0, left=Node(1, left=Node(1), right=Node(1)), right=Node(0)))
    assert count_unival_subtrees(tree) == 5
    assert count_unival_subtrees_cache(tree) == 5
