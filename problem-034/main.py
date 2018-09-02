#!/usr/bin/env python
""" Problem 34 daily-coding-problem.com """

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def find_palindrome_prefix(s: str) -> int:
    for i in range(len(s)-1, -1, -1):
        if (is_palindrome(s[:i+1])):
            return (len(s) - i - 1)

def find_palindrome(s: str) -> str:
    if is_palindrome(s):
        return s

    prefix = s[-find_palindrome_prefix(s):][::-1]
    return prefix + s

if __name__ == "__main__":
    assert find_palindrome("java") == "avajava"
    assert find_palindrome("abcba") == "abcba"
    assert find_palindrome("race") == "ecarace"
    assert find_palindrome("google") == "elgoogle"