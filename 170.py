# Student CGPA Calculator using python programming language 

print("Welcome to CGPA Calculator!")

n = int(input("Enter number of semesters: "))

total = 0

for i in range(1, n + 1):
    cgpa = float(input(f"Enter CGPA for semester {i}: "))

    if 0 <= cgpa <= 10:
        total += cgpa
    else:
        print("Invalid CGPA! Enter a value between 0 and 10.")
        break

else:
    if n > 0:
        average = total / n

        print("\n--- CGPA Report ---")
        print("Total Semesters:", n)
        print("Average CGPA:", round(average, 2))
    else:
        print("Please enter at least one semester.")
      
