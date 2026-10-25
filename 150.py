# Student Marks Analyzer using python programming language 

students = {
    "Rahul": [85, 90, 78],
    "Priya": [92, 88, 95],
    "Kiran": [70, 75, 80],
    "Anu": [60, 55, 65]
}

for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)

    print("\nStudent:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))

    if average >= 85:
        print("Grade: A")
    elif average >= 70:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
      
