#!/usr/bin/env python
""" Problem 66 daily-coding-problem.com """
import random


def toss_biased() -> bool:
    bias, toss = random.random(), random.random()
    return toss > bias


def toss_unbiased() -> bool:
    """ see John von Neumann theorem """

    toss1, toss2 = toss_biased(), toss_biased()
    if toss1 == toss2:
        return toss_biased()
    return toss1


if __name__ == "__main__":
    pass
