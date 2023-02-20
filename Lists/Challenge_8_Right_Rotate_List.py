"""
Challenge 8: Right Rotate List
Given a list, can you rotate its elements by one index from right to left? Implement your solution in Python and see if your code runs successfully!

We'll cover the following

Problem Statement
Input
Output:
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

Input
A list and a positive number by which to rotate that list

Output:
The given list rotated by k elements

Sample Input#
lst = [10,20,30,40,50]
k = 3
"""

def right_rotate(lst, k):
    if not lst:
        return []
    for _ in range(k):
        new_list = [lst[-1]]+lst[:-1]
        lst=new_list
    return lst




def right_rotate(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(4)))
