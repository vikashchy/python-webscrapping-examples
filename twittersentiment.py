import tweepy
from textblob import TextBlob
# import urllib2
import json
import datetime
import time

# We enter API Auth coordonates in order to retrieve data from Twitter

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

brand = "Google"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Google')

print("############################################################")
print("## HERE IS THE TWITTER PEOPLE FEELING ABOUT",brand,"##")
print("############################################################")
for tweet in public_tweets:
    print(tweet.text)

    # TextBlob Devide text into words and tags
    # This technic is called Bags of words model: Tokenize the text and use a lexicon of sentiment to rate the words
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


print("############################################################")
print("## HERE IS THE TWITTER PEOPLE FEELING ABOUT",brand,"##")
print("############################################################")
# We enter API Auth coordonates in order to retrieve data from Twitter
app_id = ""
app_secret = "" # DO NOT SHARE WITH ANYONE!
access_token = app_id + "|" + app_secret
page_id = 'Google'


def request_fb_server(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try:
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception :
            print ()
            # time.sleep(5)

            print ("Error for URL %s: %s" % (url, datetime.datetime.now()))


    return response.read()


def testFacebookPageFeedData(page_id, access_token):

    # We build the URL
    link = "https://graph.facebook.com/v2.6"

    # We can navigate through the FB Graph in order to retreive specific data
    # Facebook Graph Doc: https://developers.facebook.com/docs/graph-api
    fb_graph_node = "/" + page_id + "/posts"
    parameters = "/?access_token=%s" % access_token
    url = link + fb_graph_node + parameters



    # We retrieve data from Facebook Graph
    data = json.loads(request_fb_server(url))
    last_fb_post=1
    for x in xrange(last_fb_post,last_fb_post+11): # Select the last 10 posts
        if data['data'][x]['message'] != "":
            post = data['data'][x]['message']
            print (post)
            blobpost = TextBlob(post)
            print (blobpost.sentiment)

testFacebookPageFeedData(page_id, access_token)
