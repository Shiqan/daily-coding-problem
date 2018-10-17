#!/usr/bin/env python
""" Problem 78 daily-coding-problem.com """
import heapq
from typing import List


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return " -> ".join([str(i.value) for i in self])

    def __eq__(self, other):
        return self.value == other.value and self.next == other.next


def merge_linked_lists(lists: List[Node]) -> List[Node]:
    h = [(l.value, idx) for idx, l in enumerate(lists) if l]
    heapq.heapify(h)
    head = cur = Node(None)
    while h:
        val, idx = heapq.heappop(h)
        cur.next = Node(val)
        cur = cur.next
        node = lists[idx] = lists[idx].next
        if node:
            heapq.heappush(h, (node.value, idx))
    return head.next


if __name__ == "__main__":
    lists = [
        Node(1, Node(2, Node(4))),
        Node(3, Node(4, Node(5))),
        Node(2, Node(3, Node(6)))
    ]

    expected = Node(
        1, Node(2, Node(2, Node(3, Node(3, Node(4, Node(4, Node(5, Node(6)))))))))
    result = merge_linked_lists(lists)
    assert result == expected
