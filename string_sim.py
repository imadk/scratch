'''
Created on 2013-11-09

@author: Imad Khoury
'''
from __future__ import division

from nltk import distance
from nltk.tokenize import word_tokenize


def sentence_edit_dist(s1, s2):    
    """Computes the levenshtein distances between s1 and s2
    where 1.0 is most similar and 0.0 most dissimilar"""
    edit_dist = distance.edit_distance(s1, s2) 
    final_dist = edit_dist / max( len(s1), len(s2) )
    print "----->Edit: " + str(1 - final_dist)
    return 1 - final_dist

def sentence_jaccard_dist(s1, s2):    
    """Computes the jaccard distance between s1 and s2
    where 1.0 is most similar and 0.0 most dissimilar"""
    s1 = word_tokenize(s1)
    s2 = word_tokenize(s2)
    jacc_dist = distance.jaccard_distance(set(s1), set(s2)) 
    print "----->Jaccard: " + str(1 - jacc_dist)
    return 1 - jacc_dist

def sentence_cross_dist(s1, s2, l_weight = 0.15, j_weight = 0.85):    
    """Computes a mixed crossed distance between s1 and s2
    using a linear combination of the edit distance and 
    the jaccard distance"""
    jacc_dist = sentence_jaccard_dist(s1, s2)
    edit_dist = sentence_edit_dist(s1, s2) 
    #Pick the highest distance and put more weight on it
    if jacc_dist <= edit_dist:
        j_weight = 0.15
        l_weight = 0.85
    final_dist = j_weight * jacc_dist + l_weight * edit_dist
    return final_dist

def sentence_sim():
    """Takes two sentences (or texts more generally)
    and computes a mixed cross-distance"""
    sentence_1 = raw_input ("Enter 1st sentence: ").strip(' \t\n\r')
    sentence_2 = raw_input ("Enter 2nd sentence: ").strip(' \t\n\r')
   
    if len(sentence_1) == 0 or len(sentence_2) == 0:
        print "Empty string detected. Please try again!\n"
        sentence_sim()
        
    sen_dist = sentence_cross_dist(sentence_1, sentence_2)
    print "|__________________________The sentence similarity is: " + str(sen_dist) + "\n"
    sentence_sim()
    
    
sentence_sim()



