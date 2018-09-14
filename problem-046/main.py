#!/usr/bin/env python
""" Problem 46 daily-coding-problem.com """

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def find_palindromic_substring(s: str) -> str:
    if is_palindrome(s):
        return s

    for i in range(len(s), -1, -1):
        for j in range(len(s) - i + 1):
            if is_palindrome(s[j:i+j]):
                return s[j:i+j]

if __name__ == "__main__":
    assert find_palindromic_substring("aabcdcb") == "bcdcb"
    assert find_palindromic_substring("bananas") == "anana"
