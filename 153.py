# Expense Tracker using python programming language 

expenses = []

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append((name, amount))

total = sum(amount for name, amount in expenses)

print("\n--- Expense Summary ---")

for name, amount in expenses:
    print(name, ":", round(amount, 2))

print("Total expenses: ₹", round(total, 2))

if expenses:
    highest = max(expenses, key=lambda item: item[1])
    print("Highest expense:", highest[0], "- ₹", highest[1])
  
