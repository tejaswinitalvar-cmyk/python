# Email Validator using python programming language 

email = input("Enter your email address: ")

if "@" in email and "." in email:
    if email.index("@") > 0 and email.index(".") > email.index("@") + 1:
        if email.endswith(".com") or email.endswith(".in"):
            print("Valid Email Address!")
        else:
            print("Invalid Email Extension!")
    else:
        print("Invalid Email Address!")
else:
    print("Invalid Email Address!")
  
