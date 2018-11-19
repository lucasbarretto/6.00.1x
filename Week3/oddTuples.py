#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:43:32 2017

@author: josebarretto
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    
    for x in range(len(aTup)):
        if (x+1) % 2 != 0:
            newTup = newTup + (aTup[x],)
    return newTup