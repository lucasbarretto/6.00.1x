#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:15:30 2018

@author: josebarretto
"""

def genPrimes():
    primes = []
    
    num = 2
    
    
    while True:
        
        isPrime = True
                
        for prime in primes:
            if num % prime == 0:
                isPrime = False
                num += 1
                    
        if isPrime:
            primes.append(num)
            next = num
            num += 1
            yield next