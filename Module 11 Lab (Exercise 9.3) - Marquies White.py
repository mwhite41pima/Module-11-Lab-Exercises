# # Marquies White
# Module 11 Lab (Exercise 9.3)
# CIS129
# 11/17/2024

import csv

# function to input student names and grades
def input_information():
    print()
# creates and opens a csv file
with open('grades.csv', mode="w", newline="") as info:
    writer = csv.writer(info)
    # creates the loop to input student info
    while True:
        firstname = input("Enter the student's first name.")
        lastname = input("Enter the student's last name.")
        try: 
            # asks for the grades inputs
            exam1grade = float(input("Enter the student's first test grade."))
            exam2grade = float(input("Enter the student's second test grade."))
            exam3grade = float(input("Enter the student's third test grade."))
        except ValueError:
            print("Please enter a valid number.")
        # writes the inputs to the csv
        writer.writerow([firstname, lastname, exam1grade, exam2grade, exam3grade])
        # continues the loop to allow for other students to be added
        continue_input = input("Do you want to enter another student? (Y/N)")
        if continue_input == "N":
            break
# calls the function
input_information()