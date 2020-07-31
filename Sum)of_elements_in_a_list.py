# If you think about it, many standard operations can be thought of in terms of recursion.
# Take the sum of elements, for example. It's not hard to notice that the sum of the first element of a list and the sum of the rest of the elements in this list gives you the sum of all the elements.
# Taking this fact into account, finish the template for a recursive function list_sum(). 
# It takes a list of numbers as its input and outputs their sum. You need to determine the condition for the base case and the action that needs to be performed in the recursive step.
# Sample Input 1: 
# 5
# Sample Output 1:
# 5
# Sample Input 2:
# 5 2 3
# Sample Output 2:
# 10

def list_sum(some_list):
    if some_list == []:
        return 0
    if len(some_list) == 1:  # base case
        return some_list[0]
    return some_list.pop() + list_sum(some_list)
    
# def list_sum(some_list):
#    if some_list == []:
#        return 0
#    if len(some_list) == 1:  # base case
#        return some_list[0]
#    return some_list[0] + list_sum(some_list[1:])
