#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:26:59 2017

@author: josebarretto
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    if exp == 0:
        return 1
    
    else:
        return base*recurPower(base, exp-1)