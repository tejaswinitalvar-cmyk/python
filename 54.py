# Check if a string starts and ends with the same character using python programming language 

text = input("Enter a string: ")

if text[0].lower() == text[-1].lower():
    print("The string starts and ends with the same character.")
else:
    print("The string does not start and end with the same character.")
