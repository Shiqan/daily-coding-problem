#!/usr/bin/env python
""" Problem 6 daily-coding-problem.com """

class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.both = prev ^ next

    def prev(self, next):
        return self.both ^ next

    def next(self, prev):
        return self.both ^ prev

class XORLinkedList:
    def __init__(self):
        self.memory = [Node(None, -1, -1)]

    def head(self):
        return 0, -1, self.memory[0]

    def add(self, value):
        current_node_index, previous_node_index, current_node = self.head()
        while True:
            next_node_index = current_node.next(previous_node_index)
            if next_node_index == -1:
                break
            previous_node_index, current_node_index = current_node_index, next_node_index
            current_node = self.memory[next_node_index]

        new_node_index = len(self.memory)
        current_node.both = previous_node_index ^ new_node_index
        self.memory.append(Node(value, current_node_index, -1))

    def get(self, index):
        current_index, previous_index, current_node = self.head()
        for _ in range(index + 1):
            previous_index, current_index = current_index, current_node.next(previous_index)
            current_node = self.memory[current_index]
        return current_node.value

if __name__ == "__main__":
    l = XORLinkedList()
    for i in range(10):
        l.add(i)

    assert l.get(2) == 2