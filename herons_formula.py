# Write a program that calculates the area of a triangle by its three sides using Heron's formula. Do not round the result.

from math import sqrt

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2

s = sqrt(p * (p - a) * (p - b) * (p - c))

print(s)
