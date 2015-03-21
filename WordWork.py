#!/usr/bin/env python

# coding: utf-8

# 
# PART 1: WORD FREQUENCIES 
# 

# In[1]:


# Linux Command from Anaconda (Prints inline): ipython notebook --matplotlib=inline

import os

HOME = os.environ['HOME'] # Finds computer home on Linux
WORKINGDIR = HOME + '/anaconda/Examples/WordWork' # Points to Anaconda package

WORDINPDIR = WORKINGDIR + '/wc_input' # Points to Input text files
WORDOUTDIR =  WORKINGDIR + '/wc_output' # Points to output word counts


# In[2]:


os.chdir(WORDINPDIR) #Sets current directory
Line = open('First.txt', 'r') 
print "Example: " + Line.read()


# In[3]:


allFiles = os.listdir(WORDINPDIR) # Stores files in wc_input
print(allFiles)


# In[4]:


Lines = ""
for line in allFiles:
    Lines += open(line, 'r').read().lower() #Sets to lower case
    
print(Lines)


# In[5]:


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


# In[6]:


import matplotlib
# % matplotlib inline # For plotting in iPython Notebook

# Plots the counts
import matplotlib.pyplot as plt

plt.figure(figsize = [15,5])
plt.bar(range(len(wordFreq)), wordFreq.values(), align="center")
plt.xticks(range(len(wordFreq)), list(wordFreq.keys()))
plt.show()



# In[7]:


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



# 
# PART TWO: RUNNING MEDIANS
# 

# In[8]:


allFiles = sorted(allFiles) # Sorts files by name 
print(allFiles)


# In[9]:


os.chdir(WORDINPDIR) #Sets current directory

#For setting max frequency
Line = open(allFiles[0], 'r').read() # Reads in first line sorted by file name

tokenizer = RegexpTokenizer(r'\w+') # Inspired by: Rob Malouf on StackOverflow
firstLine = len(tokenizer.tokenize(Line)) # Counts non-punctuation words in first by sort

print(tokenizer.tokenize(Line))

str(firstLine) + ' Words in first line' # Word count in first sorted line


# In[10]:


lineLen = {}
for i in range(len(allFiles)): 
    lineLen[i] = len(tokenizer.tokenize(open(allFiles[i], 'r').read()))
        
#Returns sorted line counts 
for key, value in lineLen.items():
    print allFiles[key], value
  
    


# In[21]:


# Prints cumulative medians

med = {}
for i in range(len(lineLen.values())):
    med[i] = np.median(lineLen.values()[:i + 1])
    
for median in med.values():
    print median


# In[34]:


# Saves to med_result.txt
os.chdir(WORDOUTDIR)

# Removes text if already exists
if os.path.exists('med_result.txt'):
    os.remove('med_result.txt')
    
wc = open('med_result.txt', 'w')

# Inspired from "bytesoftly.com" & "truppo" on StackOverflow
wc.write(str(med.values()))

wc.close()

