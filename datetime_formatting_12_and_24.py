# Write a function format_time that takes a datetime object and formats its time component in a 24-hour format and a 12-hour format. 
# The function doesn't return anything, instead, it should print the resulting strings, first the one with a 24-hour clock and then a 12-hour one. 

from datetime import datetime


def format_time(datetime_obj):
    date_string_24 = datetime_obj.strftime("%H:%M")
    date_string_12 = datetime_obj.strftime("%I:%M")
    print(f"24h {date_string_24}")
    print(f"12h {date_string_12}")
