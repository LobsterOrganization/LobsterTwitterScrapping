# This is a sample Python script. MONGODB mdp: twitter123456
import tweepy
import config

import json

# client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
# query = 'écologie OR ecologie -is:retweet lang:fr'
# response = client.search_recent_tweets(query=query, end_time="2022-06-12T00:00:00Z", tweet_fields="created_at",max_results=100)
# print(response)



def searchTweets(client, query):

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations','created_at'], max_results=100)

    tweet_data = tweets.data
    results = []

    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            obj['date'] = tweet.created_at
            results.append(obj)
    else:
        return ''
    
    return results

client = getClient()

dictionnaire="(écologie OR énergie OR éolienne OR éléctricité OR transport) lang:fr"

tweets = searchTweets(client, dictionnaire)



if len(tweets) > 0:
    for x in tweets:
        print(x)
else:
    print('no matchning tweets found')