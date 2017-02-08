
def unique():
    uniqlines = set(open('Summary/positive.txt').readlines())    
    bar = open('Summary/positive_unique.txt', 'w').writelines(set(uniqlines))
    
    uniqlines = set(open('Summary/negative.txt').readlines())    
    bar = open('Summary/negative_unique.txt', 'w').writelines(set(uniqlines))