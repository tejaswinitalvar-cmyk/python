# Daily Water Intake Tracker using python programming language 

goal = 2000  # Daily goal in ml
total_water = 0

print("Welcome to Water Intake Tracker!")

n = int(input("How many times did you drink water today? "))

for i in range(n):
    amount = int(input("Enter water amount in ml: "))
    total_water += amount

print("\n--- Water Intake Report ---")
print("Total Water Consumed:", total_water, "ml")
print("Daily Goal:", goal, "ml")

if total_water >= goal:
    print("Congratulations! Daily goal completed.")
else:
    remaining = goal - total_water
    print("You need", remaining, "ml more to reach your goal.")
  
