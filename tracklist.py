# Joe defined a dictionary listing his favorite artists, their albums, and the song from each of the albums. It looks as follows:
# 
# tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                       "On the Other Side": "Samara"},
#           "Cure": {"Disintegration": "Lovesong",
#                    "Wish": "Friday I'm in love",
#                    "Seventeen Seconds": "A Forest"}}
# Joe's tastes can change, though.
# 
# Your task is to define a tracklist() function that would take several keyword arguments representing musicians and dictionaries with albums and songs as values. For the example above, the call of this function will look as follows:
# 
# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
# The function should print the values from the dictionary in the following form:
# 
# Woodkid
# ALBUM: The Golden Age TRACK: Run Boy Run
# ALBUM: On the Other Side TRACK: Samara
# Cure
# ALBUM: Disintegration TRACK: Lovesong
# ALBUM: Wish TRACK: Friday I'm in love
# ALBUM: Seventeen Seconds TRACK: A Forest

def tracklist(**tracks):
    for artist, albums in tracks.items():
        print(artist)
        for album, song in albums.items():
            print(f"ALBUM: {album} TRACK: {song}")
