# There's a file seasons.txt that looks like this:
# Spring
# Summer
# Autumn
# Winter
# What will be the value of the variable favorite_season?

seasons_file = open('seasons.txt', 'r', encoding='utf-8')

seasons = seasons_file.readlines()
favorite_season = seasons[2]

seasons_file.close()

# A: Autumn\n
