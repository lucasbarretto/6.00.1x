#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:30:08 2017

@author: josebarretto
"""
init_balance = float(input("balance: "))
annualInterestRate = float(input("anual interest rate: "))

payment = 0
balance = init_balance

def annualbalance(balance, aIR, payment):
    for i in range(12):
        balance -= payment
        interest = annualInterestRate/12.0 * balance
        balance += interest
    return balance
    
while balance > 0:
    balance = init_balance
    payment += 10
    balance = annualbalance(balance, annualInterestRate, payment)
    
print("Lowest payment:", payment)