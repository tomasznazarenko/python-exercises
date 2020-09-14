# In a galaxy far, far away, there is a planet where biology works in mysterious ways. 
# Not only do the planet's residents inherit genes from their parents, but also parts of their identity. Each parent contributes one half.
# Read two strings with parental genetic information, find their IDs and calculate the mean.

one_ancestor = input()
other_ancestor = input()
new_alien = (id(one_ancestor) + id(other_ancestor)) / 2
