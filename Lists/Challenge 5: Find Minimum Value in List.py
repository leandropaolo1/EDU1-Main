"""
Problem Statement#
Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input:#
A list of integers

Output:#
The smallest number in the list
"""

def find_minimum(arr):
    arr.sort(reverse=False)
    return arr[0]

find_minimum([100, 12, 34, 40])