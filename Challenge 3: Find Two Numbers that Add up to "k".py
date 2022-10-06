"""
Problem Statement#
In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

Input#
A list and a number k

Output#
A list with two integers a and b that add up to k

"""


lst = [1, 21, 3,20,61, 14, 5, 60, 7, 6]
k = 81

def find_sum(lst,k):
    matches = []
    lst2 = lst

    for first_pair in lst:
        for second_pair in lst2:
            pair_sum = first_pair + second_pair
            if pair_sum == k:
                matches.append(first_pair)

    print(matches)
    return matches

find_sum(lst,k)