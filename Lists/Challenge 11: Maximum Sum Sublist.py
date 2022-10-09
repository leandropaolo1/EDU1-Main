"""
Problem statement#
Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.

"""

def find_max_sum_sublist(lst): 
  print(lst)
  sum_list = []

  for i in range(len(lst)):
    int_sum = sum(lst[i:])
    sum_list.append(int_sum)
    print(lst[i:], int_sum)
  
  sum_list.sort(reverse = True)
  return sum_list[0]


lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
find_max_sum_sublist(lst)



"""
Solution:

"""
def find_max_sum_sublist(lst): 
    print(lst)
    best = cur = 0
    for i in lst:
        print(cur, cur+i)
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best
