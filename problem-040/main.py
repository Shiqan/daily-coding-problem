#!/usr/bin/env python
""" Problem 40 daily-coding-problem.com """
from typing import List


def find_non_duplicated(arr: List[int], occurs: int) -> int:
    ones = 0
    twos = 0
     
    for i in arr:
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        twos = twos | (ones & i)
         
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        ones = ones ^ i
         
        # The common bits are those bits 
        # which appear third time. So these
        # bits should not be there in both 
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)
         
        # Remove common bits (the bits that 
        # appear third time) from 'ones'
        ones &= common_bit_mask
         
        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
    return ones

if __name__ == "__main__":
    assert find_non_duplicated([6, 1, 3, 3, 3, 6, 6], 3) == 1
    assert find_non_duplicated([13, 19, 13, 13], 3) == 19