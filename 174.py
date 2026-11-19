# Student Result Management System using python programming language 

print("Welcome to Student Result Management System!")

name = input("Enter student name: ")

subjects = ["Python", "DBMS", "Java", "Maths", "Computer Networks"]

total = 0

for subject in subjects:
    marks = int(input("Enter marks in " + subject + ": "))
    total += marks

percentage = total / len(subjects)

print("\n--- Student Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")
  
