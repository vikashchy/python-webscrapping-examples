import wikipedia
import Quandl
import  pandas as pd
print(Quandl)
#  Search Wikipedia #
print(wikipedia.search("Vikash",results=10,suggestion=False))
#  Open WIKI PAGE #
vik = wikipedia.page("Narendra Modi")
print(vik.content)
# open File in a particular encoding #
namo = open('Namo.txt',mode='w+',encoding='UTF-8')
# dump wiki contents to file #
namo.write(str(vik.content))
wordcount={}      # ------> for word count maintain a dictionary #
# search for content in test file #
for word in namo.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print(word,wordcount)
namo.close();
print(wordcount.keys())     # ----> Print Keys of a dictionary#
# Prepare a dataframe from dictionary #
df=pd.DataFrame.from_dict(wordcount,orient='index')
# print(df.head())
print(df)

