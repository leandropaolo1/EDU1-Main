"""
Problem Statement#
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:#
A list of numbers (could be floating points or integers)

Output:#
A list such that each index has a product of all the numbers in the list except the number stored at that index.
"""


def find_product(lst):
    context = []
    print(lst)
    for i in range(len(lst)):
        first_pair = lst[i+1:]
        second_pair = lst[:i]
        lst2 = first_pair + second_pair
        result=1
        for x in lst2:
            result = result * x
        context.append(result) 
    return context

find_product([1, 2, 3, 4])