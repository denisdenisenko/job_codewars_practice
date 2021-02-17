"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"


"""

"""
# -*- coding: utf-8 -*-
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
"""


def solution(string, markers):
    new_string = ""
    indexer = 0
    for i in string:
        if i in markers:
            while i != "\n":
                pass
        new_string += i
        indexer += 1

    print(new_string)


def solution2(string, markers):
    new_string = ""
    indexer = 0
    for i in range(len(string)+1):
        if indexer == len(string)-1:
            print(new_string)
            return new_string
        if string[indexer] in markers:
            while string[indexer] != '\n':
                indexer += 1
                if indexer == len(string) - 1:
                    print(new_string)
                    return new_string
        new_string += string[indexer]
        indexer += 1

    print(new_string)
    return new_string


solution2("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
