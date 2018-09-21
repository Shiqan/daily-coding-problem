#!/usr/bin/env python
""" Problem 53 daily-coding-problem.com """

class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, value):
        self.inbox.append(value)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def __repr__(self):
        return str(self.inbox + self.outbox)


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)

    print(queue)
    for i in range(10):
        assert queue.dequeue() == i
