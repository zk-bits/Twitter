# Twitter

This is the first release of hopefully many, at the moment you have to run three files one after the other in the following order, please don't kill me ill fix these in the next couple of days I developed this in a bit less than 10 days while also working full time, so please bare with me while I perfect it enough to be considered user friendly.

The program is made up at the moment of three files and will get a fourth one eventually


The first file ‘Tweety.py’ is in charge of downloading a set o tweets the user can define a search term or several according to the tweepy  user guide

	#This line filter Twitter Streams to capture data by keywords
    	stream.filter(languages=["en"], track=[("#TuesdayMotivation")])

you can also tweak the number of tweets you want to retrieve.

  #while the number of tweets is less than 5 it continues to write them into the file created above
            if self.num_tweets < 1000 :                
                tf.write(data)     
                return True
The tweets will be saved into a file called ‘fetched_tweets.csv’. There is an example of this already in place in case the user doesn't have internet connection and wants to try it out anyway. If on the other hand you do want to retrieve your own tweets you do have to delete that file. Don´t worry its automatically generated.

The second file is in charge of classifying the tweets as positive or negative. This file is called ‘Analyser.py’. This basically cleans the tweets and then applies a naïve Bayes Classifier  to them, it then divides the tweets into a positive and a negative file. There is a folder called ‘Training’ that contains a file called ‘Training_data’ which is what the bases classier uses to train itself before it actually classifies the tweets. it is only made up of around 7,000 tweets so feel free to add your own if you have it I really couldn't afford to spend too much time searching for a huge classified set of tweets.

Now here is where it gets ever so slightly tricky, given this two files, one would think that you could summarise them quite easily and just get an over view of the whole, however Natural language is not even close to being so advance so we have to depend on heuristic methods. This is the second pat of the application and the more tricky one.

The Third file, ‘Re-ordering.py' contains two important parts, the first one consists of comparing each tweet to the rest of the tweets in the file and comparing the string distance, while this is currently has an O(n)^2 it can be improved a lot then again I haven't had the time as of today of implementing this. The output of the comparison is a list of lists in which all the comparisons are shown as percentages. For whoever is interested in why the O() complexity can be reduced:
	Given sentences A-D we can visualise the relationships in the following way
  
	    A    B    C   D	
	A   1   .3   .4  .5
	B  .3    1   .2  .1
	C  .4   .2    1  .7
 	D  .5   .1   .7   1
  
This means that for every extra column that we enter the cosine of, the time to process the rest of the table becomes exponentially smaller. Note the numbers are not actual output and are just there for illustration.

On the second part of this file, we transform the list into a numpy array. We then use this as input for the KMeans algorithm, which clusters the array into the desired number of Centres, or paragraphs. This amount can be determined here:	
		X=np.array(Matrix)            
		k=12 #This determines the number of centroids
		kmeans = KMeans(n_clusters=k, random_state=0).fit(Matrix)

The rest of this readMe file, simply specifies what is left to implement and how I would go on about it if I had the time to do so, ill update this periodically to reflect the amount I have advanced.

Within file three we will create k number of paragraphs and write them into a new file, 

We will then apply the summarisation algorithm in the 4th file to get a comprehensive overview of the topic we have searched.


You have to have installed a couple of modules for this to actually work 
tweepy 
argparse 
string 
json 
Keys as k 
csv
re 
operator 
math
itertools
numpy 
matplotlib.pyplot
nltk
from nltk - punkt
from tweepy   Stream 
from tweepy   OAuthHandler 
from tweepy.streaming   StreamListener 
from collections - Counter
from sklearn.cluster - KMeans
