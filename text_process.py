'''
Created on 2013-11-09

@author: Imad
'''
from __future__ import division

import nltk
from nltk.corpus import wordnet as wn
from collections import OrderedDict
#For dataframes - unused yet 
#import pandas as pd 
#from sklearn.feature_extraction.text import CountVectorizer         


def stop_strip(ss):
    """Strips string ss from stopwords"""
    nltk.data.path.append("/nltk_data/")
    sp = ss.split()
    swords = set(nltk.corpus.stopwords.words('english'))
    for s in sp:
        if (s in swords):
            sp.remove(s)
    sp = " ".join(sp)
    return ss, sp        
    
#def freq_table(ss, show_table=False):
    """computes a frequency table for word-tokenized 
    stemmed and stopped strings - (ss is a string)"""

    
    
ss, sp = stop_strip("This sentence  has  a bunch of stop words that need to be removed!")
print ss
print sp

