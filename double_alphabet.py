# Write a program that creates a dictionary, in which keys are latin letters, and values are their doubling:
# {a: aa, b: bb, ..., z: zz}
# Save this dictionary in the variable double_alphabet.

from string import ascii_lowercase

double_alphabet = {letter: letter * 2 for letter in ascii_lowercase}


# from string import ascii_lowercase
#
# alphabet = list(ascii_lowercase)
# double_alphabet = dict(zip(alphabet, [letter * 2 for letter in alphabet]))
