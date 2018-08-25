#!/usr/bin/env python
""" Problem 27 daily-coding-problem.com """

def validate(s: str) -> bool:
    def is_closing_tag(s: str) -> bool:
        return s in ")]}"
    
    def closes(s: str) -> bool:
        if s == ")":
            return "("
        if s == "]":
            return "["
        return "{"

    balance = []
    for i in s:
        if is_closing_tag(i):
            if balance[-1] != closes(i):
                return False
            
            balance.pop()
        else:
            balance.append(i)
    
    return not balance

if __name__ == "__main__":
    assert validate("([])[]({})") == True
    assert validate("(((())))") == True
    assert validate("([)]") == False
    assert validate("((()") == False