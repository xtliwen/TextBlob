# -*- coding: utf-8 -*-
import string

def strip_punc(s):
    '''Removes punctuation from a string.'''
    return s.translate(string.maketrans("", ""), string.punctuation)

def lowerstrip(s):
    '''Makes text all lowercase and strips punctuation and whitespace.'''
    return strip_punc(s.lower().strip())