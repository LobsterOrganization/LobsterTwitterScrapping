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
    c = tweepy.Cursor(api.search,
                       q=search,
                       include_entities=True).items()
    while True:
        try:
            tweet = c.next()
            # Insert into db
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break
    return api

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

ids = []
apiAuth = authenticate()
for page in tweepy.Cursor(apiAuth.get_follower_ids, screen_name="DebieCste").pages():
    ids.extend(page)
    time.sleep(2)

print(len(ids))

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