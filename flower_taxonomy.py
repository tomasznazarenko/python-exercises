# Ronald is filling up his dataset with new data to classify species of Iris flowers better. Define a function add_iris() to help him a bit.
# 
# The parameters for each new sample include id_n identifying a flower, species, petal_length and petal_width. Apart from species, which should be a string, all the mentioned parameters will have a numerical value: either an integer (id_n) or a float (petal_length, petal_width). Collect other keyword arguments in case new features appear.
# 
# Your function should add a new key-value pair into an existing dictionary called iris. Predictably, id_n will serve as a key, and its value should be a dictionary with the rest of specified parameters.
# 
# For example, after calling the function for the first time add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac') the dictionary iris will look like this {0: {'species': 'Iris versicolor', 'petal_length': 4.0, 'petal_width': 1.3, 'petal_hue': 'pale lilac'}}. Pay attention to the last pair that represents a new feature.

iris = {}


def add_iris(id_n, species, petal_length, petal_width, **other_features):
   iris[id_n] = {"species": species, "petal_length": petal_length, "petal_width": petal_width, **other_features}}
