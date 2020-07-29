# Anthony goes for a walk every morning, and a special app counts how many meters he walks. Calculate how much Anthony walks on average per day.
# The input list with Anthony's walks looks something like this:
# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]
# Your task is to write a program that would access the values, count the mean, and print the result rounded to an integer: in this case. for example, the output would be 2871.

print(round(sum(walk["distance"] for walk in walks) / len(walks)))
