# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:38:55 2026

@author: priyanka
"""

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise Exception("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)
except Exception as e:
    print("Error:", e)