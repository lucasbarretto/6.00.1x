#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:10:30 2017

@author: josebarretto
"""

balance = float(input("balance: "))
annualInterestRate = float(input("anual interest rate: "))
monthlyPaymentRate = float(input("monthly payment rate: "))

for i in range(12):
    minMonthlyPayment = monthlyPaymentRate*balance
    balance -= minMonthlyPayment
    interest = annualInterestRate/12.0 * balance
    balance += interest
    
print(round(balance, 2))