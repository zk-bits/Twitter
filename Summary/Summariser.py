import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

def final():    
    with open('Summary/paragraph.txt' ) as pt:
        text = pt.readlines()
        for k in text:
            print summarize(k)
        

            
