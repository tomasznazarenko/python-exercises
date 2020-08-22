# Suppose that list_1 and list_2 are two lists of the same length containing numbers.
# Define a function my_product(list_1, list_2) that would construct and return a new list 
# containing the result of the element-wise product of the elements of list_1 and list_2. 
# Element-wise product means that we multiply the first element of list_1 by the first element of list_2, 
# the second element by the second, etc

def my_product(list_1, list_2):
    return list(map(lambda x, y: x * y, list_1, list_2))
