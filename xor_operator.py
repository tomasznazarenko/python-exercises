# Implement a XOR operator that can work with objects of any type.
# Its behaviour should be the following:
# 
#     if the operands are both truthy or both falsy, return False,
#     if one operand is truthy and the other operand is falsy, return the truthy one.
# 
# Write your code inside the xor() function. Your program shouldn't read any input or call the function, just implement it.

def xor(a, b):
    return a or b if (a and not b) or (not a and b) else False
