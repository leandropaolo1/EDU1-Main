"""
Challenge 7: Find Second Maximum Value in a List
Given a list of size n, can you find the second maximum element in the list? Implement your solution in Python and see if your output matches the correct output!

We'll cover the following

Problem Statement
Input:
Output:
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function find_second_maximum(lst) which returns the second largest element in the list.

Input:
A List

Output:
Second largest element in the list

Sample Input
[9,2,3,6]
Sample Output
6

Coding Exercise
Take a close look and design a step-by-step algorithm first before jumping on to the implementation. This problem is designed for your practice, so try to solve it on your own first. Good Luck!
"""


def find_second_maximum(lst):
    if not lst:
        return None

    lst.sort()
    return lst[-2]

def find_second_maximum(lst):
    largest_number = lst[0]
    second_largest_number = lst[1]

    if second_largest_number > largest_number:
        largest_number = lst[1]
        second_largest_number = lst[0]

    for ele in lst:
        if ele > largest_number:
            second_largest_number = largest_number
            largest_number = ele
        if ele > second_largest_number and ele < largest_number:
            second_largest_number = ele
        
    return second_largest_number

        

def find_second_maximum(lst):
   if (len(lst) < 2):
       return
   # initialize the two to infinity
   max_no = second_max_no = float('-inf')
   for i in range(len(lst)):
       # update the max_no if max_no value found
       if (lst[i] > max_no):
           second_max_no = max_no
           max_no = lst[i]
       # check if it is the second_max_no and not equal to max_no
       elif (lst[i] > second_max_no and lst[i] != max_no):
           second_max_no = lst[i]
   if (second_max_no == float('-inf')):
       return
   else:
       return second_max_no


print(find_second_maximum([9, 2,4,6,3,2,9, 2,4,6,3,2,3, 6,23,12,3, 6]))