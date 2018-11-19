#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:09:10 2017

@author: josebarretto
"""

s = 'azcbobobeggh'
a = 0
count = 0

for a in range(len(s) - 2):
    if s[a] == 'b' and s[a+1] == 'o' and s[a+2] == 'b':
        count += 1

print("Number of times bob occurs is: " + str(count))