#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:51:51 2017

@author: josebarretto
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a == b:
        return a
    
    elif a > b:
        return gcdRecur(a-b, a)
    
    elif b > a:
        return gcdRecur(a, b-a)