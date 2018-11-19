#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:15:56 2017

@author: josebarretto
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result  = 1
    
    while exp > 0:
        result *= base
        exp -= 1
    
    return result
