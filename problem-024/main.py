#!/usr/bin/env python
""" Problem 24 daily-coding-problem.com """

class Node:
    def __init__(self, value, parent, locked=False, left=None, right=None):
        self.value = value
        self.parent = parent
        self.locked = locked
        self.left = left
        self.right = right
        self.locked_descendants_count = 0

    def is_locked(self):
        return self.locked
    
    def _can_lock_or_unlock(self):
        if self.locked_descendants_count > 0:
            return False

        cur = self.parent
        while cur:
            if cur.is_locked():
                return False
            cur = cur.parent
        return True

    def lock(self):
        if self._can_lock_or_unlock():
            self.locked = True

            cur = self.parent
            while cur:
                cur.locked_descendants_count += 1
                cur = cur.parent

            return True
        return False
    
    def unlock(self):
        if self._can_lock_or_unlock():
            self.locked = False
            
            cur = self.parent
            while cur:
                cur.locked_descendants_count -= 1
                cur = cur.parent

            return True
        return False

if __name__ == "__main__":
    root = Node("root", None)
    root.left = Node("left-1", root)
    root.right = Node("right-1", root)

    root.right.left = Node("left-2", root.right)
    root.right.right = Node("right-2", root.right)

    root.left.left = Node("right-2", root.left)
    root.left.right = Node("left-2", root.left)


    assert root.lock() == True
    assert root.unlock() == True

    assert root.left.left.lock() == True
    assert root.lock() == False




    
