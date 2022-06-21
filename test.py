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
    # c = tweepy.Cursor(api.search,
    #                    q=search,
    #                    include_entities=True).items()

    return api

# def authenticateCursor():
#     auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
#     auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)    
#     api = tweepy.API(auth)
#     c = tweepy.Cursor(api.search,
#                        q=search,
#                        include_entities=True).items()

#     return c

def searchActor(name):
    
    apiAuth = authenticateCursor()
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

# ids = []
# apiAuth = authenticate()
# for page in tweepy.Cursor(apiAuth.get_follower_ids, screen_name="bcvorwerck").pages():
#     ids.extend(page)
#     time.sleep(60)
    
# print(ids)

ids = []
apiAuth = authenticate()
for page in tweepy.Cursor(apiAuth.get_follower_ids, screen_name="bcvorwerck").items():
    ids.append(page)
    time.sleep(60)
    
print(ids)

# my_followers = []
# apiAuth = authenticate()
# for follower in tweepy.Cursor(apiAuth.followers, screen_name).items():
#     my_followers.append(follower.screen_name)
#     time.sleep(2)

for user in tweepy.Cursor(apiAuth.get_friends, screen_name="bcvorwerck").items():
    my_followers.append(user.screen_name)


for user in tweepy.Cursor(apiAuth.get_followers, screen_name="bcvorwerck").items():
    my_followers.append(user.screen_name)


# print(my_followers)

# userID = "EmmanuelMacron"
# resultss = []
    
# for user in userID:
#     resultss.extend(searchTweets(user))


# print(searchActor(userID))

# èèèè

def search_oneUser_info(actorName):
    # userName = "EmmanuelMacron"
    resultss = []
    
    resultss.extend(searchActor(actorName))
        
    return resultss

    
# resultat = search_oneUser_info("EmmanuelMacron")

# print(resultat)

# datafr = pd.DataFrame(resultat)
# datafr.to_csv('tabUserv1.csv')