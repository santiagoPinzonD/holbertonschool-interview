#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n
"""


def minOperations(n):
    """
    method that calculates the fewest number of
    operations needed to result
    in exactly n H characters in the file
    """
    list1 = []
    if n < 4:
        return 3
    if n % 2 == 0:
        sum1 = 2
    else:
        sum1 = 3
    for x in range(1, n + 1):
        if x < 3:
            list1.append(x)
        elif sum1 == 3:
            if x == 3:
                list1.append(x)
            list1.append(list1[-1] + sum1)
            if list1[-1] == n:
                break
        else:
            if x > 2:
                list1.append(list1[-1] + sum1)
                if list1[-1] == n:
                    break
    result = len(list1) + 1
    if result % 2 == 0 and result > 6:
        result -= 1
    return result

