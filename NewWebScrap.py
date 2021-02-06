import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import urlopen


def importTicker():
    df = pd.read_excel("BSE.xlsx")
    print(df["Scrip\nCode"][0:2])
    return df["Scrip\nCode"][0:2]


def fetchWebpage():
    for tick in importTicker():
        try:
            url = "http://www.screener.in/company/" + str(tick)
            # page = requests.get(url)
            # print(page.content)
            filename = "D:\\BSE\\" + str(tick) + ".html"
            f = open(filename, 'wb')
            f.write(urlopen(url).read())
            f.close()
        except:
            print("Exception Occured for {}".format(tick))


def viewCurrent():
    for tick in importTicker():
        url = "http://www.screener.in/company/" + str(tick)
        html = urlopen(url)
        bs4Obj = BeautifulSoup(html, "lxml")
        stk = bs4Obj.find("div", {"class": "D(ib) Fw(200) Mend(20px)"})
        print(str(tick) + "--->" + str(stk))
        time.sleep(1)


if __name__ == "__main__":
    viewCurrent()
    # importTicker()
    fetchWebpage()



