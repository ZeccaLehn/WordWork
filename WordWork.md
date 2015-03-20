

PART 1: WORD FREQUENCIES



    
    # Linux Command from Anaconda (Prints inline): ipython notebook --matplotlib=inline
    
    import os
    
    HOME = os.environ['HOME'] # Finds computer home on Linux
    WORKINGDIR = HOME + '/anaconda/Examples/WordWork' # Points to Anaconda package
    
    WORDINPDIR = WORKINGDIR + '/wc_input' # Points to Input text files
    WORDOUTDIR =  WORKINGDIR + '/wc_output' # Points to output word counts



    
    os.chdir(WORDINPDIR) #Sets current directory
    Line = open('First.txt', 'r') 
    print "Example: " + Line.read()


    Example: So call a big meeting,
    



    
    allFiles = os.listdir(WORDINPDIR) # Stores files in wc_input
    print(allFiles)


    ['Third.txt', 'First.txt', 'Fourth.txt', 'Second.txt']



    
    Lines = ""
    for line in allFiles:
        Lines += open(line, 'r').read().lower() #Sets to lower case
        
    print(Lines)


    make every who holler,
    so call a big meeting,
    make every who shout shout.
    get everyone out out,
    



    
    # Note setup from http://www.nltk.org/install.html
    # sudo pip install -U numpy 
    # Downloaded then ran...
    # nltk.download()
    import nltk
    import nltk.tokenize
    from nltk import FreqDist
    from nltk.tokenize import RegexpTokenizer 
    
    tokenizer = RegexpTokenizer(r'\w+') # Inspired by: Rob Malouf on StackOverflow
    tokens = tokenizer.tokenize(Lines) # Returns a list of words without punctuation
    
    # For setting max frequency
    wordFreq = FreqDist(tokens)
    maxFreq = wordFreq[FreqDist(tokens).max()] + 1
    
    wordFreq





    FreqDist({'make': 2, 'who': 2, 'shout': 2, 'every': 2, 'out': 2, 'a': 1, 'everyone': 1, 'call': 1, 'big': 1, 'so': 1, ...})




    
    import matplotlib
    # % matplotlib inline # For plotting in iPython Notebook
    
    # Plots the counts
    import matplotlib.pyplot as plt
    
    plt.figure(figsize = [15,5])
    plt.bar(range(len(wordFreq)), wordFreq.values(), align="center")
    plt.xticks(range(len(wordFreq)), list(wordFreq.keys()))
    plt.show()
    



![png](https://github.com/ZeccaLehn/WordWork/blob/master/WordWork_6_0.png)



    
    ## Writes frequency table to 'wc_result.txt' ##
    
    import os
    import re
    import numpy as np
    import pandas as pd
    
    os.chdir(WORDOUTDIR) #Sets current directory
    
    # Removes text if already exists
    if os.path.exists('wc_result.txt'):
        os.remove("wc_result.txt")
        
    wc = open('wc_result.txt', 'w')
    
    # Inspired from "bytesoftly.com" & "truppo" on StackOverflow
    for key in sorted(wordFreq):
         wc.write('%s\n' % ("%s: %s" % (key, wordFreq[key])))
    wc.close() 
    
    
    #Returns key-value table
    pd.Series(wordFreq)
    





    a           1
    big         1
    call        1
    every       2
    everyone    1
    get         1
    holler      1
    make        2
    meeting     1
    out         2
    shout       2
    so          1
    who         2
    dtype: int64




PART TWO: RUNNING MEDIANS



    
    allFiles = sorted(allFiles) # Sorts files by name 
    print(allFiles)


    ['First.txt', 'Fourth.txt', 'Second.txt', 'Third.txt']



    
    os.chdir(WORDINPDIR) #Sets current directory
    
    #For setting max frequency
    Line = open(allFiles[0], 'r').read() # Reads in first line sorted by file name
    
    tokenizer = RegexpTokenizer(r'\w+') # Inspired by: Rob Malouf on StackOverflow
    firstLine = len(tokenizer.tokenize(Line)) # Counts non-punctuation words in first by sort
    
    print(tokenizer.tokenize(Line))
    
    str(firstLine) + ' Words in first line' # Word count in first sorted line


    ['So', 'call', 'a', 'big', 'meeting']





    '5 Words in first line'




    
    lineLen = {}
    for i in range(len(allFiles)): 
        lineLen[i] = len(tokenizer.tokenize(open(allFiles[i], 'r').read()))
            
    #Returns sorted line counts 
    for key, value in lineLen.items():
        print allFiles[key], value
      
        

    First.txt 5
    Fourth.txt 5
    Second.txt 4
    Third.txt 4



    
    # Prints cumulative medians
    
    med = {}
    for i in range(len(lineLen.values())):
        med[i] = np.median(lineLen.values()[:i + 1])
        
    for median in med.values():
        print median

    5.0
    5.0
    5.0
    4.5



    
    # Saves to med_result.txt
    os.chdir(WORDOUTDIR)
    
    # Removes text if already exists
    if os.path.exists('med_result.txt'):
        os.remove('med_result.txt')
        
    wc = open('med_result.txt', 'w')
    
    # Inspired from "bytesoftly.com" & "truppo" on StackOverflow
    wc.write(str(med.values()))
    
    wc.close()
