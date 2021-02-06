import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
from bs4 import BeautifulSoup
# print the first 500 characters of the HTML
print(r.text[0:500])
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})
len(results)





