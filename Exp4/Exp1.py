# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:05:11 2026

@author: User
"""


n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
 num = int(input(f"Enter element {i+1}: ")) 
 numbers.append(num)

# Calculating sum and average
total = sum(numbers)
average = total / n if n > 0 else 0
print("List:", numbers)
print("Sum of elements:", total)
print("Average of elements:", average)
