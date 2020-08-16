# You are given a list containing letters of a name. 
# Print them out as a string with these chars separated by hyphens and with an exclamation point in the end. 
# Do so using arguments of the print() function!

name = ['M', 'A', 'R', 'C', 'O']
print(*name, sep='-', end='!')
