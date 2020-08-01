# Imagine that suddenly all machines have gone insane and simple multiplication is not working for natural numbers anymore. 
# Let's write a new function for this task recursively!
# Reduce this problem to a smaller one with the recursive step, and then stop recursion with the base step.

def multiply(a, b):
    if b == 1:  # base case
        return a
    return a + multiply(a, b - 1)
