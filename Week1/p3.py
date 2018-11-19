#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:23:47 2017

@author: josebarretto
"""

s = 'abcbdc'
a = 0
p = ''

for a in range(len(s)):
    start = a
    finish = a
    
    for i in range(a, len(s) - 1):
        if ord(s[i + 1]) >= ord(s[i]):
            finish = i + 1
        else:
            break
    
    size = finish - start
    
    if a == 0:
        max_size = size
        for i in range(start, finish + 1):
            p += s[i]
    
    else:
        if size > max_size:
            max_size = size
            p = ''
            for i in range(start, finish + 1):
                p += s[i]

print("Longest substring in alphabetical order is: " + p)