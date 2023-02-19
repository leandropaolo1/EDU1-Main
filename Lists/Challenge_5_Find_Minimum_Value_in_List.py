"""
Challenge 5: Find Minimum Value in List
Given a list of size (n), can you find the minimum value in the list? Implement your solution in Python and see if your output matches the expected output.

We'll cover the following

Problem Statement
Input:
Output:
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input:
A list of integers

Output:
The smallest number in the list

Sample Input
arr = [9,2,3,6]
Sample Output
2

"""


def find_minimum(arr):
    current_min = arr[0]
    for ele in arr:
        if ele < current_min:
            current_min = ele
        
    return current_min