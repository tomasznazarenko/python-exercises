 # The Fibonacci numbers were used to illustrate the growth of an idealized rabbit population that live and reproduce according to the following rules:
# 
#     the initial population is a pair of baby rabbits (a female + a male)
#     rabbits become adults at the age of one month and after another month give birth to a new pair of baby rabbits
#     these rabbits are immortal
#     a pair of adult rabbits always gives birth to one new pair (a female + a male) a month
# 
# The Fibonacci numbers tell the number of rabbit pairs after n months, meaning that after 6 months there will be 8 pairs of rabbits.
# 
# Finish the template of a recursive function that finds how many pairs of rabbits there will be after n months (the nth Fibonacci number). Here, you'll need to make multiple recursive calls inside the function!
# 
# You do NOT need to take input or call this function! 

def fib(n):
    if n <= 0:  # base case for month 0
        return 0  # the rabbits are not on a farm yet!
    if n == 1:  # base case for month 1
        return n  # a pair of baby rabbit has just arrived!
    return fib(n - 1) + fib(n - 2)
