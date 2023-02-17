"""
Challenge 4: List of Products of all Elements
Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.

We'll cover the following

Problem Statement
Input:
Output:
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:
A list of numbers (could be floating points or integers)

Output:
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input
arr = [1,2,3,4]
Sample Output
arr = [24,12,8,6]

"""


def find_product(lst):
    result = []
    my_list = lst
    for i in range(len(my_list)):
        total = 1
        current_element = my_list[i]
        other_elements = my_list[:i] + my_list[i+1:]

        if 0 in other_elements:
            result.append(0)
        else:
            for ii in other_elements:
                total *= ii
            result.append(total)

    return result
