# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:59:26 2026

@author: priyanka
"""

items = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)