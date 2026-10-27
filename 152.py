# Password Strength Checker using python programming language 

password = input("Enter your password: ")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

score = sum([
    len(password) >= 8,
    has_upper,
    has_lower,
    has_digit,
    has_special
])

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength:", strength)
