import wikipedia
import pandas as pd

vik =wikipedia.page("Narendra Modi")
namo =open('Namo.txt',mode='r',encoding='UTF-8')
# namo.write(str(vik.content))
wordcount = {}
word=''
for word in namo.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# print(word,wordcount)
# print(wordcount.keys())
df=pd.DataFrame.from_dict(wordcount,orient='index')
print(df)
df.to_csv('word.csv')
namo.close();