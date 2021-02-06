from urllib.request import urlopen
from bs4 import BeautifulSoup

nexturl = []
nexttitle = []
source = "http://www.thehindu.com"

def article(url):
    # print(url)
    for _url in url:
        para=''
        fullurl=source+_url
        try:
            # print(source.join(_url))
            page = urlopen(fullurl).read().decode("utf-8")
            soup = BeautifulSoup(page, "lxml")
            data = soup.find_all('p')
            for _data in data:
                para +=_data.text
            print(soup.title.text)
            print("\t")
            print(para)
            print("\n")
        except:
            pass
            # print("Exception for :" + _url)


def fetchlinks(source):
    page = urlopen(source).read().decode("utf-8")
    soup = BeautifulSoup(page, "lxml")
    links = soup.find_all('a')
    for _urllist in links:
        try:
            nexturl.append(_urllist.get('href'))
            nexttitle.append(_urllist.get('title'))
        except:
            pass
    return nexturl,nexttitle


def fetchallurls(nexturl):
    for _newlink in nexturl:
        try:
            newpage = urlopen(_newlink).read().decode("utf-8")
            _soup = BeautifulSoup(newpage, "lxml")
            newlink = _soup.find_all('a')
            # print(newlink.get('href'))
            for link in newlink:
                nexturl.append(link.get('href'))
                print(link.get('href'))
        except :
            pass
    return nexturl


urls,headlines = fetchlinks(source)
# print(nexturl)
fetchallurls(nexturl)
print(nexturl)
# article(urls)