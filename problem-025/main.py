#!/usr/bin/env python
""" Problem 25 daily-coding-problem.com """

def match_regex(s: str, r: str) -> bool:
    for i in range(len(r)):
        if r[i] == ".":
            s = s[1:]
            continue
        
        if r[i] == "*":
            for j in range(len(s)+1):
                if match_regex(s, (j*r[i-1]) + r[i+1:]):
                    s = s[j:]
                    break
            continue

        if r[i] != s[0]:
            return False
        
        s = s[1:]

    return not s

if __name__ == "__main__":
    # assert match_regex("", ".*") == True
    assert match_regex("abc", "abc") == True
    assert match_regex("ray", "ra.") == True
    assert match_regex("raymond", "ra.") == False
    assert match_regex("raymond", "ra.*") == True
    assert match_regex("raymond", "ra.*d") == True
    assert match_regex("chat", ".*at") == True
    assert match_regex("aaac", "a*c") == True
    assert match_regex("abcd", "abc.*") == True
    assert match_regex("abcd", "ab*d") == False