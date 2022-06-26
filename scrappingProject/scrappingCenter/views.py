from django.shortcuts import render
from django.http import HttpResponse
import tweepy
import csv
import json
import pandas as pd
from pymongo import MongoClient

# A METTRE DANS LE CONFIG (ONI ME GRONDE PAS DESSUS JE VAIS LE FAIRE APRES)

TWITTER_CONSUMER_KEY = 'IXBsOhx5JVqDH4WiScZnHvJC8'
TWITTER_CONSUMER_SECRET = '8rSBkRBy5CxE1As9S64hnHjctSPkUmZ2GnTvL3MNjoY2DTPVfi'
TWITTER_ACCESS_TOKEN = '1536977498650685440-3pCXHUtEx3m0A9MZji6yWUDQBOceUW'
TWITTER_ACCESS_TOKEN_SECRET = 'JHInPSzHxfd4tdtAp9TyfxDcjKre8H8Y0aGJczVknBoL6'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAP0kdwEAAAAA5caCys8AnDktaOytX5szfYD%2FWms%3DsPZBH2OCUXtPR4feADG7sos4frqL9BBj3cGjivJZ0TnpYCSo4A'

word_dictionnary = "(écologie OR énergie OR éolienne OR éléctricité OR transport OR nucléaire OR co2 OR carbonne OR petrole OR renouvelables OR énergies renouvelables OR chauffage électrique OR énergie fossiles OR gaz OR hydraulique OR climat OR solaire OR effet de serre OR énergie primaire OR eéologique OR énergitique OR ecologique OR recyclage OR biodiversite OR biomasse OR développement durable OR écocitoyen OR écosysteme) lang:fr"
actor_dictionnary = ["Akuo_Energy", "IFPENinnovation", "Ecologie_Gouv", "EU_Commission", "ARP_NUC","Framatome_", "ENGIE_EC", "EDF_Entreprises", "elonmusk",  "SFENorg", "Albioma", "Arkolia_EnR","EnergieCap","CNR_Officiel", "Groupe_Coriance","DalkiaWEnergy", 
                    
                    "2022lecologie" ,
                    "COP21" ,
                    "UNEPfr" ,
                    "CFigueres" ,
                    "yjado" ,
                    "algore" ,
                    "ClimateMarch15" ,
                    "CCNUCC",
                    "CPLCFrance",
                    "RACFrance", 
                    "ClimateChance" 
                ] 

# AUTHENTICATION RULES (ONI ME GRONDE PAS DESSUS, JE VAIS LE DEPLACER TKT)
def getClient():
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    return client

def authenticate():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)    
    api = tweepy.API(auth)
    return api


# GET ATTRIBUTES (ONI CA AUSSI, ME GRONDE PAS DESSUS JE VAIS LE BOUGER AUSSI)
def getretweet(id):
    api = authenticate()
    status = api.get_status(id)
    retweet_count = status.retweet_count       
    return retweet_count

def getTweet(client,id):
    tweet = client.get_tweet(id, expansions = ['author_id'], user_fields= ['username'])
    return tweet

# 1ST DATABASE
# 
# 

results = []
client = getClient()


def searchTweetsWordDictionnary(client, query):
    
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations','created_at'], max_results=100)
    tweet_data = tweets.data  
    pagination_tweets = tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=10)
    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in pagination_tweets :
            twt = getTweet(client,tweet['id'])
            username= twt.includes['users'][0].username
            retweet= getretweet(tweet.id)   
            id = tweet.id
            text = tweet.text
            date = tweet.created_at        
            line = {'USER_ID' : id, 'DATE_TIME' : date, 'USERNAME' :username , 'TWEET_TEXT':text, 'NUMBER_OF_RETWEET': retweet }                     
            results.append(line)
    else:
        return ''
    return results

 

def index(request):
    word_dictionnary="(écologie OR énergie OR éolienne OR éléctricité OR transport) lang:fr"
    client = getClient()
    tweets = searchTweetsWordDictionnary(client, word_dictionnary)
    all_tweet = pd.DataFrame(tweets)
    all_tweet.to_csv('First_Dataset.csv')    
    print(all_tweet)
    return HttpResponse("Hello world!")
# Create your views here.

