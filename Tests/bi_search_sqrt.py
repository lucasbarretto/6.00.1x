#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:28:50 2017

@author: josebarretto
"""

print("This program finds the approximate square root of a number through bisection search")
x = float(input("Choose a number: "))
epsilon = 0.0001

def bi_sqrt(s, f, x):
    
    a = (s+f)/2
    
    if abs(a**2 - x) <= epsilon:
        return a
    
    else:
        if a**2 > x:
            a = bi_sqrt(s, a, x)
            return a
        
        elif a**2 < x:
            a = bi_sqrt(a, f, x)
            return a
        
print("The approximate square root of", x, "is", bi_sqrt(1, x, x))