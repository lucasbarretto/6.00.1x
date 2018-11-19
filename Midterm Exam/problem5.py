#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:09:57 2018

@author: josebarretto
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    result = []
    
    for key in aDict:
        if aDict[key] == target:
            result.append(key)
            
    result.sort()
    return result
            