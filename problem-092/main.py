#!/usr/bin/env python
""" Problem 92 daily-coding-problem.com """
from typing import Dict, List


def course_order(courses: Dict[str, List[str]]) -> List[str]:
    def contains(list1, list2):
        return all(elem in list1 for elem in list2)

    def find_courses(courses, taken_courses):
        if not courses:
            return taken_courses

        possible_courses = [course for course, prereq in courses.items() if contains(taken_courses, prereq)]
        
        for course in possible_courses:
            del courses[course]

        taken_courses.extend(possible_courses)
        return find_courses(courses, taken_courses)

    possible_courses = [course for course, prereq in courses.items() if not prereq]
    for course in possible_courses:
        del courses[course]
    return find_courses(courses, possible_courses)


if __name__ == "__main__":
    courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
    assert course_order(courses) == ['CSC100', 'CSC200', 'CSC300']