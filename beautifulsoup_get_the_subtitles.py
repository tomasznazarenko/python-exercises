# Find and print a subtitle of the article by an index. 
# The index of the subtitle is the first line in the input, and the link to the article is the second one. 
# For example, your code should print The Definite Article for the following input:
#
# 1
# https://www.grammarly.com/blog/articles/

import requests
from bs4 import BeautifulSoup

i = int(input())
url = input()

respone = requests.get(url)
soup = BeautifulSoup(respone.content, 'html.parser')
subtitles = soup.find_all('h2')

print(subtitles[i].text)
