# Marquies White
# Module 11 Lab
# CIS129
# 11/17/2024

# function to input grades
# excercise 9.1
def input_grades():
    print()

# creates and opens grades.txt into writing mode
with open('grades.txt', mode="w") as grades:
    # creates the loop for inputting grades
    while True:
        grade = input("Enter a grade or 'done' when finished.")
        # ends the loop when sentinel value 'done' is entered
        if grade == "done":
            break
        # converts the input to a float and writes it to grades.txt
        try:
            grade = float(grade)
            grades.write(f"{grade}\n")
        # catches any valueerrors and restarts the loop
        except ValueError:
            print("Please enter a number or 'done' when finished.")

# calls the function
input_grades()

# function to read grades
# excercise 9.2
def read_grades():
    # creates a list to store all the grades
    grades = []
    # opens the grades.txt file in read only mode
    with open('grades.txt', mode='r') as grades_file:
        # creates a line for each grade
        for line in grades_file:
            # turns each grade into a float
            grade = float(line)
            # adds the grades to the list 'grades'
            grades.append(grade)
        # prints all grades in the list
        print("Individual grades:", grades)
        # calculates the total, count and average of the grades
        total = sum(grades)
        count = len(grades)
        average = total / count
        # prints each of the calculations
        print("Total:", total)
        print("Count:", count)
        print("Average:", average)
# calls the function
read_grades()
