# Student Grade Management System using python programming language

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter student marks: "))

    if 0 <= marks <= 100:
        students[name] = marks
    else:
        print("Invalid marks! Enter marks between 0 and 100.")

print("\n--- Student Grade Report ---")

for name, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print(name, "- Marks:", marks, "- Grade:", grade)
