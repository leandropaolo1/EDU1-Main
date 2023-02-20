"""
Challenge 9: Rearrange Positive & Negative Values
Given a list, can you rearrange its elements in such a way that the negative elements appear at one end and positive elements appear at the other? Solve this problem in Python and see if your code runs correctly!

We'll cover the following

Problem Statement
Output
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.

Output
A list with negative elements at the left and positive elements at the right

Sample Input
[10,-1,20,4,5,-9,-6]
Sample Output
[-1,-9,-6,10,20,4,5]
"""


def rearrange(lst):
    negative_numbers = []
    positive_numbers = []
    zeros = []
    new_array = []
    for ele in lst:
        if ele > 0:
            positive_numbers.append(ele)
        elif ele < 0:
            negative_numbers.append(ele)
        else:
            zeros.append(ele)

    new_array = negative_numbers + zeros + positive_numbers    
    return new_array

print(rearrange([10, -1, 20, 4, 5, -9, -6]))


def rearrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr != leftMostPosEle:
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))


def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


print(rearrange([10, -1, 20, 4, 5, -9, -6]))

