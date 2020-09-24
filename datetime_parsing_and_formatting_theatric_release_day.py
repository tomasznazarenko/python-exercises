# Suppose, we have a movie database and we want to extract the day of release. The entry for the date is stored like this:
# Day of release: 4 July 2019
# Your task is to finish the function that extracts the date from this string.  The function is called get_release_date. 
# It takes the release day entry in the described format (a string) and returns the corresponding datetime object.
#
# Sample Input 1:
# Day of release: 4 July 2019
# Sample Output 1:
# 2019-07-04 00:00:00

from datetime import datetime


def get_release_date(release_str):
    return datetime.strptime(release_str[16:], '%d% B% Y')
