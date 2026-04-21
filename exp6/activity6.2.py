# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:16:33 2026

@author: priyanka
"""

def mark_attendance():
    date = input("Enter date (DD-MM-YYYY): ")
    name = input("Student name: ")
    status = input("Present/Absent (P/A): ").upper()
    
    with open("attendance.txt", "a") as f:
        f.write(f"{date},{name},{status}\n")
    print("Attendance marked!")

def view_attendance():
    try:
        with open("attendance.txt", "r") as f:
            print("\nDate       | Name           | Status")
            print("-" * 35)
            for line in f:
                date, name, status = line.strip().split(",")
                print(f"{date} | {name:<14} | {status}")
    except FileNotFoundError:
        print("No attendance records yet.")

while True:
    ch = input("\n1. Mark Attendance  2. View All  3. Exit\nChoose: ")
    if ch == '1':
        mark_attendance()
    elif ch == '2':
        view_attendance()
    else:
        break