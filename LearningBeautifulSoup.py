from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.tutorialspoint.com/python/python_date_time.htm"

import sys
print(sys.path)
page = urlopen(url)
soup = BeautifulSoup(page,"html.parser")
# for tags in soup.findAll('p'):
#     print(tags.text)
# print()

