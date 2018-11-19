#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:20:16 2017

@author: josebarretto
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    x = len(aStr)//2
    
    if aStr == '':
        return False
    
    if len(aStr) == 1:
        return char == aStr
    
    if char == aStr[x]:
        return True
    
    elif char > aStr[x]:
        return isIn(char, aStr[x+1:])
    
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[:x])