from django.shortcuts import render
import tweepy
import got
import json
#Import the necessary methods from tweepy library

from tweepy import Cursor

from config import get_twitter_client


# Create your views here.


def get_tweets(request):
    client = get_twitter_client()
    tweets = Cursor(client.search, q='labourparty').items(10)
    
    context_dict = {'tweets': tweets }

    def printTweet(descr, t):
		print descr
		print "Username: %s" % t.username.encode('utf-8')
		print "Retweets: %d" % t.retweets
		print "Text: %s" % t.text.encode('utf-8')
		print "Mentions: %s" % t.mentions
		print "Hashtags: %s\n" % t.hashtags.encode('utf-8')
    
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(20)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[10]
    printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)
    

    return render(request, 'twitter/tweets.html', context=context_dict)