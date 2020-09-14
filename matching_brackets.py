# As you have probably noticed, most code editors check if you used the right number of brackets in your code.
# Write a simple brackets checker that, given a string, prints 'OK' if all the brackets are used correctly, and 'ERROR' otherwise.
# Don't forget to check that the brackets are in the right order (opening before closing).
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/#:~:text=One%20approach%20to%20check%20balanced,%2C%20return%20Balanced%20otherwise%2C%20Unbalanced.

from collections import deque

text = input()
stack = deque()

for char in text:
    if char == '(':
        stack.append(1)
    if char == ')' and len(stack) == 0:
        stack.append(1)
        break
    elif char == ')':
        stack.pop()

print('ERROR' if len(stack) > 0 else 'OK')
