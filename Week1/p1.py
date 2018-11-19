#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:08:49 2017

@author: josebarretto
"""

s = 'artyrtyrtyertyrtyrtyirtyrtyortyrtyurtyrty'
count = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1

print("Number os vowels: " + str(count))