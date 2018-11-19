#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 01:13:35 2017

@author: josebarretto
"""

balance = float(input("Balance: "))
annualInterestRate = float(input("Anual Interest Rate: "))

def annualbalance(balance, annualInterestRate, payment):
    for i in range(12):
        balance -= payment
        interest = annualInterestRate/12.0 * balance
        balance += interest
    return balance
    
def find_payment(balance, lb, ub):
    epsilon = 0.001
    payment = (lb + ub)/2.0
    
    if abs(annualbalance(balance, annualInterestRate, payment)) <= epsilon:
        return payment
    
    elif annualbalance(balance, annualInterestRate, payment) > 0:
        return find_payment(balance, payment, ub)
    
    elif annualbalance(balance, annualInterestRate, payment) < 0:
        return find_payment(balance, lb, payment)
        

lb = balance/12.0
monthlyInterestRate = annualInterestRate/12.0
ub = (balance * (1 + monthlyInterestRate)**12)/12.0

payment = find_payment(balance, lb, ub)

print('\n' + "Lowest payment:", round(payment, 2))