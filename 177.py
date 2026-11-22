# Library Fine Calculator using python programming language

print("Welcome to Library Fine Calculator!")

days = int(input("Enter number of late days: "))

if days <= 0:
    fine = 0
elif days <= 5:
    fine = days * 2
elif days <= 10:
    fine = (5 * 2) + (days - 5) * 4
else:
    fine = (5 * 2) + (5 * 4) + (days - 10) * 5

print("\n--- Library Fine Report ---")
print("Late Days:", days)
print("Total Fine: Rs.", fine)
