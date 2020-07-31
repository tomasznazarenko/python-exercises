# In the very first year, there are 120120120 frogs in the marsh. 
# Once a year, 505050 frogs move to a nearby pond, while the remaining frogs breed so that their number doubles.
# Write a function number_of_frogs that returns this number for a given year.
#
# Sample Input 1:
# 1
# Sample Output 1:
# 120
# Sample Input 2:
# 5
# Sample Output 2:
# 420

def number_of_frogs(year):
    if year == 1:
        return 120
    return 2 * (number_of_frogs(year - 1) - 50)
