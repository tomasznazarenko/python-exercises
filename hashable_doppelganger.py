# Create a program that calculates how many objects in the list object_list have the same hash value as some other element in the list. You should **print** the number of those objects. If there are no matching hash values, the output should be 0.
# For example, if object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397], the output should be 5.
# Keep in mind that not every object in the list may be hashable!

from collections.abc import Hashable
c = 0

for i in object_list:
    if isinstance(i, Hashable):
        if object_list.count(i) > 1:
            c += 1
    
print(c)
