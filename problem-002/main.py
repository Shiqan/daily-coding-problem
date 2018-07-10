#!/usr/bin/env python
""" Problem 2 daily-coding-problem.com """
from functools import reduce


def find_product1(l):
    product = reduce(lambda x, y: x * y, l)
    result = []
    for i in l:
        result.append(product / i)
    
    return result

def find_product2(l):
    result = []
    for i in range(len(l)):
        new_list = l[:i]+l[i+1:]
        product = reduce(lambda x, y: x * y, new_list)
        result.append(product)
    
    return result



if __name__ == '__main__':
    print(find_product1([1, 2, 3, 4, 5]))
    print(find_product1([3, 2, 1]))

    print(find_product2([1, 2, 3, 4, 5]))
    print(find_product2([3, 2, 1]))