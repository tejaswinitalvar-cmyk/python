# Student Attendance Tracker using python programming language 

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Present or Absent (P/A): ").upper()

    students[name] = status

present = 0
absent = 0

print("\n--- Attendance Report ---")

for name, status in students.items():
    if status == "P":
        print(name, "- Present")
        present += 1
    else:
        print(name, "- Absent")
        absent += 1

total = present + absent

if total > 0:
    percentage = (present / total) * 100
else:
    percentage = 0

print("\nTotal Students:", total)
print("Present:", present)
print("Absent:", absent)
print("Attendance Percentage:", round(percentage, 2), "%")
