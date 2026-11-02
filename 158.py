# ATM Simulator using python programming language 

balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount deposited successfully!")
            print("New balance: ₹", balance)
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance: ₹", balance)
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice. Try again.")
      
