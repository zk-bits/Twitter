import re
import math
import itertools
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as pyplot



#first understadn this code so that we can manipulate it.
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
with open("positive.txt", "r") as pt:
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
                
    for i, x in enumerate(Matrix):
        if v in x:
            with open("positive relations.txt", "a") as pt:
                X=np.array(Matrix)
                print X
                print i                   
                if (max(Matrix[y])!=0.0 or max(Matrix[y])!=1.0 ):   
                    if(MatrixWords[i][x.index(v)]!= 1):
                        pt.write("Similarity: %s %s %s %s %s %s" % (max(Matrix[y]), "Position: ", (i,x.index(v)), "\n", MatrixWords[i][x.index(v)],"\n"))     
           
            
X=np.array(Matrix)            
k=12
kmeans = KMeans(n_clusters=k, random_state=0).fit(Matrix)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
for i in range(8):
# select only data observations with cluster label == i
    ds = X[np.where(labels==i)]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')

    print kmeans.labels_

    # plot the centroids
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
pyplot.show()
                        #Matrix[i][x.index(v)] = 0.0                
    
    # print the arary here, outside the loop
     
# get number of columns
#This is where we divide the text by sentences

#This is where we create the loop to make the paragrpahs