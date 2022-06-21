# This is a sample Python script. MONGODB mdp: twitter123456
import tweepy
import time
import json
import config
import pandas as pd
import csv

def authenticate():
    auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)    
    api = tweepy.API(auth)
    return api


def searchTweets(name):
    
    apiAuth = authenticate()
    tweets = apiAuth.user_timeline(screen_name = name, include_rts = False, tweet_mode="extended" )
    
    results=[]
     
    if not tweets is None and len(tweets) > 0:
        for tweetInfo in tweets:

            tweetId = tweetInfo.id
            tweetDate = tweetInfo.created_at
            tweetCreator = tweetInfo.user.name
            tweetText = tweetInfo.full_text
            tweetFav = tweetInfo.favorite_count
            tweetRet = tweetInfo.retweet_count

            line = {'ID': tweetId, 'DATE' : tweetDate, 'CREATOR' : tweetCreator, 'TEXT' : tweetText, 'LIKE' : tweetFav, 'RETWEET' : tweetRet}
            results.append(line)

        return results
    else:
        return ''


def searchActor(name):
    
    apiAuth = authenticate()

    user = apiAuth.get_user(screen_name = name)

    results=[]
    
    if not user is None :
        userId = user.id
        userName = user.screen_name
        userFollower = user.followers_count
        userFollow = user.friends_count
        location = user.location
        userVerified = user.verified
        userDescription = user.description
        userRt_count = user.status.retweet_count
        userFav_count = user.status.favorite_count

        line = {'ID': userId, 'NAME': userName, 'NB_FOLLOWER': userFollower, 'NB_FOLLOW': userFollow, 'LOCATION': location,
        'VERIFIED': userVerified, 'DESCRIPTION': userDescription, 'COUNT_RT': userRt_count, 'COUNT_FAV': userFav_count }
        results.append(line)

    return results
   

def search_usersTweets_info():
    userID = ["Mediavenir", "CNR_Officiel"]
    resultss = []
    
    for user in userID:
        resultss.extend(searchTweets(user))     
        
    return resultss


def search_users_info():
    listOfActeurs = ["EmmanuelMacron", "EmmanuelMacron"]
    resultss = []
    
    for userName in listOfActeurs:
        resultss.extend(searchActor(userName))     
        
    return resultss

#################################### Exécution ##################################################

resultat = search_users_info()
# resultat = search_usersTweets_info()

print(resultat)

datafr = pd.DataFrame(resultat)
datafr.to_csv('tabUserv.csv',encoding='utf-8-sig')



