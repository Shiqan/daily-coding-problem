#!/usr/bin/env python
""" Problem 29 daily-coding-problem.com """

def encode(s: str) -> str:
    result = ""
    
    while s:
        i = 0
        while i < len(s) and s[0] == s[i]:
            i += 1
        
        result = result + str(i) + s[0]
        s = s[i:]

    return result

def decode(s: str) -> str:
    s = [s[i:i+2] for i in range(0, len(s), 2)]
    return "".join([int(i) * j for i, j in s])

if __name__ == "__main__":
    assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
    assert decode(encode("AAAABBBCCDAA")) == "AAAABBBCCDAA"