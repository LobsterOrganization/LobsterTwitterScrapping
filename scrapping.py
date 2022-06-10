# This is a sample Python script.
import tweepy
import config

def retrieve_data_test():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    query = 'Macron OR Zemmour -is:retweet'
    response = client.search_recent_tweets(query=query, max_results=100)
    print(response)

retrieve_data_test()