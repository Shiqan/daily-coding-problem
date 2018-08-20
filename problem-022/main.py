#!/usr/bin/env python
""" Problem 22 daily-coding-problem.com """
from typing import List


def reconstruct(words: List[str], s: str) -> List[str]:
    check = s
    for w in words:
        check = check.replace(w, "")
        s = s.replace(w, " "+w+" ")

    if check:
        return None

    return [i for i in s.split(" ") if i]


if __name__ == "__main__":
    result = reconstruct(["quick", "brown", "the", "fox"], "helloworld")
    assert result is None

    result = reconstruct(["quick", "brown", "the", "fox"], "thequickbrownfox")
    assert result == ["the", "quick", "brown", "fox"]

    result = reconstruct(["quick", "brown", "the", "fox"], "thefoxquickbrownfox")
    assert result == ["the", "fox", "quick", "brown", "fox"]

    result = reconstruct(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond")
    assert result == ['bed', 'bath', 'and', 'beyond'] or result == ['bedbath', 'and', 'beyond']
