#!/usr/bin/env python
""" Problem 13 daily-coding-problem.com """

def find_longest_substring(k: int, s: str) -> int:
    def _helper(k: int, s: str) -> int:
        substring = ""
        distinct = 0
        for i in s:
            if i in substring:
                substring += i
            elif distinct < k:
                substring += i
                distinct += 1
            else:
                return len(substring)

        return len(substring)

    substrings = []
    for i in range(len(s)):
        substrings.append(_helper(k, s[i:]))

    return max(substrings)


if __name__ == '__main__':
    assert find_longest_substring(0, "abcba") == 0
    assert find_longest_substring(2, "abcba") == 3
    assert find_longest_substring(3, "abcba") == 5
    assert find_longest_substring(2, "abcbcba") == 5
