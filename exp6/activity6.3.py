# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:17:53 2026

@author: priyanka
"""

def add_complaint():
    complaint = input("Enter complaint: ")
    with open("complaints.txt", "a") as f:
        f.write(complaint + "\n")
    print("Complaint registered!")

def show_complaints():
    try:
        with open("complaints.txt", "r") as f:
            complaints = f.readlines()
            if not complaints:
                print("No complaints found.")
            else:
                print("\n--- All Complaints ---")
                for i, c in enumerate(complaints, 1):
                    print(f"{i}. {c.strip()}")
    except FileNotFoundError:
        print("complaints.txt not found. Add a complaint first.")

while True:
    ch = input("\n1. Add Complaint  2. Show All  3. Exit\nChoose: ")
    if ch == '1':
        add_complaint()
    elif ch == '2':
        show_complaints()
    else:
        break