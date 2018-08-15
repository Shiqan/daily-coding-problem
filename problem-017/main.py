#!/usr/bin/env python
""" Problem 17 daily-coding-problem.com """

def find_longest_absolute_path(s: str) -> int:
    def is_file(s: str):
        return "." in s
    
    directory = s.split("\n")
    
    max_lenght = 0
    root = directory[0] + "/"

    path = []
    for i in directory[1:]:
        t = i.count("\t")

        if t == 0:
            return 0

        i = i.strip()
        if  t > len(path):
            path.append(i)
        elif t == len(path):
            path[-1] = i
        else:
            path = [i]

        if is_file(i):
            max_lenght = max(max_lenght, len(root)+len("/".join(path)))
            
    return max_lenght

if __name__ == "__main__":
    assert find_longest_absolute_path("dir\n\tsubdir1\n\tsubdir2") == 0
    assert find_longest_absolute_path("dir\n\tsubdir1\nsubdir2\n\tfile.ext") == 0
    assert find_longest_absolute_path(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32