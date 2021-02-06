from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist,Counter
from heapq import nlargest
from collections import defaultdict


newssource = 'http://www.thehindu.com/news/national/other-states/six-coaches-of-nagpur-mumbai-duronto-express-derail/article19578743.ece?homepage=true'
# soup=BeautifulSoup(page,'lxml')
# print(soup.prettify())
def textWrap(url):
    page = urlopen(url).read().decode('utf-8', 'ignore')
    soup=BeautifulSoup(page,'lxml')
    # print(soup.title.text)
    article=soup.find_all('p')
    # text=''.join(map(lambda p:p.text,article))
    text = ''
    for _article in article:
        text=text + _article.text
    return text
sentence = sent_tokenize(textWrap(newssource).replace(".",". "))
print(sentence)
word_table = word_tokenize(textWrap(newssource).lower())
_stopword = set(stopwords.words('english')+ list(punctuation)+['www','hindu'])
word_sent = [words for words in word_table if words not in _stopword]
freq = Counter(word_sent)
x = nlargest(10,freq,key=freq.get)
ranking = defaultdict(int)
for i,sent in enumerate(sentence):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] +=freq[w]
sent_final = nlargest(2,ranking,key=ranking.get)
for s in sorted(sent_final):
    print(str(sentence[s]).capitalize())
