# Problem 3


This problem was asked by Google.

Given the root to a binary tree, implement <code>serialize(root)</code>, which serializes the tree into a string, and <code>deserialize(s)</code>, which deserializes the string back into the tree.
For example, given the following <code>Node</code> class</p>

``` python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:
``` python 
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```  


