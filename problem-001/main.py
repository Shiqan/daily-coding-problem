#!/usr/bin/env python
""" Problem 1 daily-coding-problem.com """

def find_sum1(l, k):
    for i in l:
        for j in l:
            if (i+j) == k:
                return True
    return False

def find_sum2(l, k):
    d = {i:i for i in l}

    for i in l:
        if (k - d[i]) in d:
            return True
    return False


if __name__ == '__main__':
    print(find_sum1([10, 15, 3, 7], 17))
    print(find_sum2([10, 15, 3, 7], 17))