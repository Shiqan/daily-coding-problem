#!/usr/bin/env python
""" Problem 86 daily-coding-problem.com """

def remove_parenthesis(s: str) -> int:
    to_be_removed = 0
    balance = []
    for i in s:
        if i == ")":
            if not balance:
                to_be_removed += 1
            else:
                if balance[-1] != "(":
                    to_be_removed += 1
                else:
                    balance.pop()
        else:
            balance.append(i)
    
    return to_be_removed + len(balance)

if __name__ == "__main__":
    assert remove_parenthesis("()())()") == 1
    assert remove_parenthesis(")(") == 2
