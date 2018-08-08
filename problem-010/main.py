#!/usr/bin/env python
""" Problem 10 daily-coding-problem.com """
from time import sleep
from typing import Any
import threading


def schedule(f: Any, n: int) -> Any:
    sleep(n/1000)
    return f()

def schedule_threaded(f: Any, n: int) -> Any:
    thread = threading.Thread(target=schedule, args=[f, n])
    thread.start()

if __name__ == '__main__':
    def _f():
        print('hello')
    schedule(_f, 5000)

    schedule_threaded(_f, 5000)
