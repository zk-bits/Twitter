#import regex
import re
import csv
import nltk

#remember to delete all tweets with a photo or link not just the photo or link
def Classify():
    #start process_tweet
    def processTweet(tweet):
        # process the tweets
        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or https?://* to URL
        tweet = re.sub(r'((www.[^\s]+)|(https[^\s]+))','',tweet)
        #Convert @username to AT_USER
        tweet = re.sub(r'@[^\s]+','',tweet)
        #Remove additional white    spaces
        tweet = re.sub(r'[\s]+', ' ', tweet)
        
        tweet = re.sub(r'text:"','', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #trim
        tweet = tweet.strip('\'"')
        #get rid of the retweets in the text
        tweet = tweet.strip('rt ')
        return tweet
    #end
    
    #initialize stopWords
    stopWords = []
    
    #start replaceTwoOrMore
    def replaceTwoOrMore(s):
        #look for 2 or more repetitions of character and replace with the character itself
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)
    #end
    
    #start getStopWordList
    def getStopWordList(stopWordListFileName):
        #read the stopwords file and build a list
        stopWords = []
        stopWords.append('AT_USER')
        stopWords.append('URL')
    
        fp = open(stopWordListFileName, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stopWords.append(word)
            line = fp.readline()
        fp.close()
        return stopWords
    #end
    
    #start getfeatureVector
    def getFeatureVector(tweet):
        featureVector = []
        #split tweet into words
        words = tweet.split()
        for w in words:
            #replace two or more with two occurrences
            w = replaceTwoOrMore(w)
            #strip punctuation
            w = w.strip('\'"?,.')
            #check if the word stats with an alphabet
            val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            #ignore if it is a stop word
            if(w in stopWords or val is None):
                continue
            else:
                featureVector.append(w.lower())
        return featureVector
    #end
    
    def extract_features(tweet):
        tweet_words = set(tweet)
        features = {}
        for word in featureList:
            features['contains(%s)' % word] = (word in tweet_words)
        return features
    
    inpTweets = csv.reader(open('Training/Training.csv', 'rd'), delimiter=',', quotechar='|')
    stopWords = getStopWordList('stopwords.txt')
    featureList = []
    
    # Get tweet words
    tweets = []
    for row in inpTweets:
        sentiment = row[0]
        tweet = row[1]
        processedTweet = processTweet(tweet)
        featureVector = getFeatureVector(processedTweet)
        featureList.extend(featureVector)
        tweets.append((featureVector, sentiment));
    #end loop
    
    # Remove featureList duplicates
    featureList = list(set(featureList))
    
    # Extract feature vector for all tweets in one shote
    training_set = nltk.classify.util.apply_features(extract_features, tweets)
    
    NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
    
    
    with open ('text_tweets.txt','r') as tweets:
        for tweet in tweets:
            processedTestTweet = processTweet(tweet)
            sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet.decode('unicode_escape').encode('ascii','ignore'))))
            #print processedTestTweet.decode('unicode_escape').encode('ascii','ignore')
            #print sentiment
            with open('Summary/positive.txt','a') as pt:
                if sentiment == "positive":
                    pt.write(processedTestTweet.decode('unicode_escape').encode('ascii','ignore') + "\n")
            with open('Summary/negative.txt','a') as nt:
                if sentiment=="negative":
                    nt.write(processedTestTweet.decode('unicode_escape').encode('ascii','ignore') + "\n")    
                    
            
                    
    
    
