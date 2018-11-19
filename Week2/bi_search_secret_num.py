#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:12:34 2017

@author: josebarretto
"""

print("Please think of a number between 0 and 100!")
start = 0
finish = 100
ans = ''
guess = (start+finish)//2

while ans != 'c':
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if ans == 'l':
        start = guess
        
    elif ans == 'h':
        finish = guess
        
    elif ans == 'c':
        print("Game over. Your secret number was:", guess)
        
    else:
        print("Sorry, I did not understand your input.")
    
    guess = (start + finish)//2