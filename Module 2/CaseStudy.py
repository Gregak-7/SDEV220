# Name: Greg Kocal
# File Name: CaseStudy.py
# Description: Program to check if a student is on the Dean's List or Honor Roll

while True:
    last_name = input("Enter student's last name: ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(first_name, last_name + " is on the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name + " is on the Honor Roll.")