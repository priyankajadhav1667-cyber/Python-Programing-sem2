# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:08:57 2026

@author: priyanka
"""

def add_expense():
    date = input("Enter date (DD-MM-YYYY) or press Enter for today: ")
    if not date:
        date = datetime.date.today().strftime("%d-%m-%Y")
    amount = float(input("Enter expense amount: "))
    desc = input("Enter description: ")
    
    with open("expenses.txt", "a") as f:
        f.write(f"{date},{amount},{desc}\n")
    print("Expense added!")

def monthly_total():
    month = input("Enter month to calculate (MM-YYYY): ")
    total = 0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                date, amount, desc = line.strip().split(",", 2)
                if date[3:] == month:  # match MM-YYYY part
                    total += float(amount)
        print(f"Total expense for {month}: ₹{total}")
    except FileNotFoundError:
        print("No expenses file found yet.")
                    
