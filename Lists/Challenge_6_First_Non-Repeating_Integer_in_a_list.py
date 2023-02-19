""""
Challenge 6: First Non-Repeating Integer in a list
Given a list, find the first integer which is unique in the list. Unique means the number does not repeat and appears only once in the whole list. Implement your solution in Python and see if it runs correctly!

We'll cover the following

Problem Statement
Input
Output
Sample Input
Sample Output
Coding Challenge
Problem Statement
Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

Input
A list of integers

Output
The first unique element in the list

Sample Input
[9,2,3,2,6,6]
Sample Output
9
Coding Challenge
Take a close look and design a step-by-step algorithm first before jumping on to the implementation. This problem is designed for your practice, so try to solve it on your own first. Good Luck!

"""


def find_first_unique(lst):
    if not lst:
        return None
    
    unique_list = []
    ununique_list = []

    for ele in lst:
        if ele not in unique_list:
            unique_list.append(ele)

        else:
            unique_list.remove(ele)

    return unique_list[0]


def find_first_unique(lst):
    if not lst:
        return None
    
    count_dict = {}
    for ele in lst:
        if ele not in count_dict:
            count_dict[ele] = 1
        else:
            count_dict[ele] += 1

    for ele in lst:
        if count_dict[ele] == 1:
            return ele

    return None


print(find_first_unique([9, 2, 3, 2, 6, 6]))


