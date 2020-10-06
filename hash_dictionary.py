# Write a program that creates a dictionary of objects as keys and their hash values as values. Objects are stored in the list objects. 
# The resulting dictionary should be called objects_dict. Do not print anything.
# Some objects in the objects list may be unhashable. This means that you cannot calculate their hash values and add them as dictionary keys. 
# Make sure to skip such objects when creating the objects_dict.

from collections.abc import Hashable

objects_dict = {}

for obj in objects:
    if isinstance(obj, Hashable):
        objects_dict[obj] = hash(obj)
