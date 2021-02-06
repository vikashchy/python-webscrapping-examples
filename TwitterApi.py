import tweepy
from textblob import TextBlob
consumer_key = 'r0TteGZqU8xPjisTtid4oQXfg'
consumer_secret = 'yafL2Bj38Ob5kOmWlsMKUFXgzjasZ1si0VzIUSIhsShWQtR98I'
access_token = '592971627-9dVnO0vBuor87uE4AGLgKfzvypni8j0wFNy2pVay'
access_token_secret = 'SwOY7tbqlUTmdzqHZBM7oDYpJ7nHzgzzLucSNBh1sIu0J'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

results=api.search('#BJPCorruptedMCD')
# results = api.user_timeline(id='@narendramodi',count=1)
for result in results:
        print(result.text)
        analysis=TextBlob(result.text)
        print(analysis.sentiment)
        # print(result.place)
        # print(result.source)
        # print(result.description)