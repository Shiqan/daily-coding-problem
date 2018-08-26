#!/usr/bin/env python
""" Problem 28 daily-coding-problem.com """
from typing import List


def justify(words: List[str], k: int) -> List[str]:
    def justified(words: List[str], k: int) -> str:
        required = k - len("".join(words))

        if len(words) == 1:
            return "{:<{}}".format(words[0], k)

        spaces = len(words) - 1
        space_len = required // spaces
        first_space = space_len + (required - (space_len * spaces))

        return words[0] + first_space*" " + (" "*space_len).join(words[1:])

    result = []
    while words:

        if len(words) == 1:
            result.append(justified(words, k))
            break

        tmp = []
        while len(" ".join(tmp + words[:1])) <= k and words:
            tmp += words[:1]
            words = words[1:]
            
        result.append(justified(tmp, k))

    return result


if __name__ == "__main__":
    assert justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16) \
        == ["the  quick brown",
            "fox  jumps  over",
            "the   lazy   dog"]

    assert justify(["This", "is", "an", "example", "of", "text", "justification."], 16) \
        == ["This    is    an",
            "example  of text",
            "justification.  "]

        