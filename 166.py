# Personal Habit Tracker using python programming language 

habits = {}

n = int(input("How many habits do you want to track? "))

for i in range(n):
    habit = input("Enter habit name: ")
    status = input("Did you complete it today? (yes/no): ").lower()

    habits[habit] = status

completed = 0
not_completed = 0

print("\n--- Daily Habit Report ---")

for habit, status in habits.items():
    if status == "yes":
        print(habit, "- Completed")
        completed += 1
    else:
        print(habit, "- Not Completed")
        not_completed += 1

print("\nTotal Habits:", n)
print("Completed:", completed)
print("Not Completed:", not_completed)

if n > 0:
    percentage = (completed / n) * 100
    print("Completion Rate:", round(percentage, 2), "%")
  
