# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:40:17 2026

@author: priyanka
"""
try:
    age = int(input("Enter your age: "))
    if age <= 0 or age > 120:
        raise ValueError("Invalid age entered!")
    else:
        print("Registration successful!")
except ValueError as e:
    print("Error:", e)
