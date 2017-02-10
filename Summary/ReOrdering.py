import re
import math
import itertools
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as pyplot

def ReOrdering():
    #this is the method used to get the string distance between tweets.
    WORD = re.compile(r'\w+')
    def get_cosine(vec1, vec2):
        intersection =  set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator
    
    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)
    
    #count the number of tweets set it to a variable and then set it as the length of this or  what ever
    #This is where the text comes from
    with open("Summary/positive_unique.txt", "r") as pt:
        lines = pt.readlines()
        # Count how many lines we have
        count = len(lines)
        # Create a count * count size matrix
        Matrix = [[1 for x in range(count)] for y in range(count)] 
        MatrixWords= [[1 for x in range(count)] for y in range(count)] 
        v = max(Matrix[y])        
        # Loop through lines assigning x as the number of line we're on and lineA as it's text
        for x, lineA in enumerate(lines):
            vectorA = text_to_vector(lineA)
            # Loop through lines again assigning y as the number of line we're on and lineB as it's text
            for y, lineB in enumerate(itertools.islice(lines, count - x)):
                vectorB = text_to_vector(lineB)
                cosine = get_cosine(vectorA, vectorB)
                v = max(Matrix[y])    
                if(x!=y):
                    #print lineA, lineB, "\n Cosine:", cosine, "\n"
                    MatrixWords[x][y]= (lineA,lineB)
                    Matrix[count-1-y][count-1-x]=get_cosine(vectorA, vectorB)
                    Matrix[x][y]=get_cosine(vectorA, vectorB)
                    #print x,y
                    #print MatrixWords[x][y]
                    v = max(Matrix[y])           
                else:
                    Matrix[x][y] = 0.0   
                    x=y
    
    X=np.array(Matrix)            
    k=12    
    kmeans = KMeans(n_clusters=k, random_state=0).fit(Matrix)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    for i in range(k):
    # select only data observations with cluster label == i
        ds = X[np.where(labels==i)]
        # plot the data observations
        pyplot.plot(ds[:,0],ds[:,1],'o')
        #print kmeans.labels_
    
        # plot the centroids
        lines = pyplot.plot(centroids[i,0],centroids[i,1],'k')
        # make the centroid x's bigger
        pyplot.setp(lines,ms=15.0)
        pyplot.setp(lines,mew=2.0)
        data = {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
        print data
        
    pyplot.show();  
    
    with open('Summary/positive_unique.txt' ) as pt:
        with open('Summary/paragraph.txt', 'w') as pt_out:
            lines = pt.readlines()
            for k, paragraph in data.iteritems():
                pt_out.write('\n')      
                for line in paragraph:
                    pt_out.write(lines[line].replace('\n', '. '))                    

                
    
    


