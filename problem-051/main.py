#!/usr/bin/env python
""" Problem 51 daily-coding-problem.com """
import random
from typing import List


def shuffle_cards(cards: List[int]) -> List[int]:
    for i in range(len(cards)-1, 0, -1):
        j = random.randint(0,i)
        cards[i], cards[j] = cards[j],cards[i]

    return cards

if __name__ == "__main__":
    cards = [i for i in range(51)]
    print(shuffle_cards(cards))

    # show with monte carlo the chances?
