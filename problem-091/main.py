#!/usr/bin/env python
""" Problem 91 daily-coding-problem.com """
import dis


original_functions = []
new_functions = []
for i in range(10):
    original_functions.append(lambda: i)
    new_functions.append(lambda i=i: i)


if __name__ == "__main__":
    for f in original_functions:
        print(f())
    dis.dis(original_functions[0])

    for f in new_functions:
        print(f())
    dis.dis(new_functions[0])
