# Given a person's name as a keyword argument and their height as its value, declare a function tallest_people(). It should print the names of the tallest people along with their heights.
# 
# If there are several names, sort them alphabetically. Also, pay attention to the output format: Name : height.
# 
# You are not supposed to handle input or call tallest_people(), just implement this function.
# 
# Sample Input 1:
# Jackie 176
# Wilson 185
# Saersha 165
# Roman 185
# Abram 169
# 
# Sample Output 1:
# Roman : 185                                                                               
# Wilson : 185


def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    most_tall = [key for key, value in kwargs.items() if value == max_height]
    most_tall.sort()
    for key in most_tall:
        print(f"{key} {kwargs[key]}")

        
# def tallest_people(**people):
#     for name, height in sorted(people.items()):
#         if height == max(people.values()):
#             print(name, ":", height)

        
tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
