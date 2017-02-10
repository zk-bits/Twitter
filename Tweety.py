import tweepy 
from tweepy import Stream 
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener 
import time
import argparse 
import string 
import json 
import Keys as k 
import csv
import re 
import operator  
import os

#This is a basic listener that just prints received tweets to stdout. 
class StdOutListener(StreamListener):

    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        #Initializes the tweet count. 
        self.num_tweets = 0

    def on_data(self, data):
        #print data
        #Creates a file called fetched_tweets
        with open('fetched_tweets.csv','a') as tf:
            #increases the number of tweets by one.
            self.num_tweets += 1
            #while the number of tweets is less than 30 it continues to write them into the file created above
            if self.num_tweets < 500:
                    tf.write(data)
            #When the number of tweets exceeds the one in the if statement it closes the connection and exits the progrm
            else:                                   
                with open("fetched_tweets.csv", 'r') as csvfile:
                # get number of columns
                    for line in csvfile.readlines():
                        array = line.split(',')
                        first_item = array[0]                
                    num_columns = len(array)
                    csvfile.seek(0)             
                    reader = csv.reader(csvfile, delimiter=',')
                    #we retrieve all the information from the third element, which contains the actual text tweets.
                    included_cols = [3] 
                    for row in reader:
                        content= (list(row[i] for i in included_cols))   
                        #We append the tweets to a text file
                        with open('text_tweets.txt','a') as tt:
                            for s in content:
                                tt.write(s + "\n")
                                #Print s                                 
                    return False
                            
    def on_error(self, status):
        print status      
        

def main():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(k.consumer_key, k.consumer_secret)
    auth.set_access_token(k.access_token, k.access_secret)
    stream = Stream(auth, l)


    #This line filter Twitter Streams to capture data by keywords
    stream.filter(languages=["en"], track=[("Valentine")])
