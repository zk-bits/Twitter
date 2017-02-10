import Tweety as tw
import Analyser as anl
import Summary.ReOrdering as rord
import Summary.Summariser as smry

#Firstly we run the Tweety class, to retrwive the tweets, and copy just the actual text into a text file
print "\n Retrieving Tweets"
#tw.main()
print "\n Retrieving Tweets: √"


print "\n Classifying Tweets"
#We now clean up the data in the text file, the tweets, and we then apply a naïve Bayes Classifier, which divides the tweets into a positive and a negative file.
#anl.Classify()
print "\n Classifying Tweets: √"

 
print "\n Reordering Tweets and arranging them into paragraphs"
#We then create an array of the similarity that each tweet has to all the other tweets and divide them into paragraphs accordingly
#rord.ReOrdering()
print "\n Reordering Tweets and arranging them into paragraphs: √"
 
 
print "\n Summarising files:"
#The summary of both, positive and negative, files is made using the gensim.summarization, which is a variation of the TextRank algorithm, for this exercise, we will have to assume the tweets make gramatical sense
smry.final()
print "\n Summarising files:√"


print "\n Done. Check the 'final.txt'  file to get the overview of twitters views on your selected topic."




