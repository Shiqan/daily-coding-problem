#!/usr/bin/env python
""" Problem 11 daily-coding-problem.com """
from typing import Any, Dict, List


class Node:
    def __init__(self, char, children, is_word=False):
        self.char = char
        self.children = children
        self.is_word = is_word


def preprocess(words: List[str]) -> Node:
    def _helper(node: Node, word: str):
        if not word:
            node.is_word = True
            return 

        char = word[0]
        if char not in node.children:
            new_node =  Node(char, {})
            node.children[char] = new_node
            return _helper(new_node, word[1:])

        return _helper(node.children[char], word[1:])

    root = Node("", {})

    for word in words:
        _helper(root, word)

    return root

def prefixed_with(q: str, tree: Node) -> List[str]:
    def _helper(tree: Node, prefix: str) -> List[str]:
        results = []

        for char in tree.children:
            if tree.children[char].is_word:
                results.append(prefix+char)
            results +=  _helper(tree.children[char], prefix+char)
        
        return results

    for char in q:
        tree = tree.children[char]
    
    return _helper(tree, q)


if __name__ == '__main__':
    query = 'de'
    strings = ['dog', 'deer', 'deal']

    # assert [i for i in strings if i.startswith(q)] == ['deer', 'deal']

    tree = preprocess(strings)
    results = prefixed_with(query, tree)
    assert results == ['deer', 'deal']


    query = 'p'
    strings = ['python', 'java', 'c++', 'php', 'ruby', 'go', 'swift', 'kotlin', 'scala', 'lua', 'perl']

    tree = preprocess(strings)
    results = prefixed_with(query, tree)
    assert sorted(results) == sorted(['python' , 'php', 'perl'])

    results = prefixed_with("", tree)
    assert sorted(results) == sorted(strings)

