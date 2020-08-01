# Write a recursive function rec_sum() that takes some natural number n as its input and outputs the sum of first n natural numbers.

def rec_sum(n):
    if n == 1:
        return 1
    return n + rec_sum(n - 1)
