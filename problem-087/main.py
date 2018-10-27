#!/usr/bin/env python
""" Problem 87 daily-coding-problem.com """
from collections import namedtuple
from typing import List

Rule = namedtuple('Rule' , ["start", "direction", "end"])

def validate_rules(rules: List[str]) -> bool:
    rules = [Rule(rule.split(" ")[0], rule.split(" ")[1], rule.split(" ")[2]) for rule in rules]
    rules.sort(key=lambda x: x.direction)
    return rules


if __name__ == "__main__":
    rules = [
        "A N B",
        "B NE C",
        "C N A",
    ]
    assert validate_rules(rules) == False

    rules = [
        "A NW B", 
        "A N B",
    ]
    assert validate_rules(rules) == True