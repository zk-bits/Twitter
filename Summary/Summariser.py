import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

def final():
    text = """" 
    ephenking: today's bummer: trump screws up our relationship with australia. bt i miss feeding my little friend  . australia. the islands australia is sending its refugees from are plagued by scandals  see here . oure: a failed muslim ban. euters: live: trump will allow australia deal over refugees to continue with extreme vetting - white house. watch here:. last year - gop obstruction. this year - gop global damage control. y'all ready to impeach the loser yet? resist. ephenking: today's bummer: trump screws up our relationship with australia. participate in msnbc live: honor refugee pledge to australia with microsoft pulse. join and vote. itchellreports: someone please tell white house australia has more troops fighting isis in iraq than any other ally + has fought at ou". arkpygas: @realdonaldtrump you should build a wall on the border with australia. 
    """ 
    
    summarize(text)