# Digital Wallet Simulator using python programming language 

balance = 1000
transactions = []

while True:
    print("\n===== DIGITAL WALLET =====")
    print("1. Check Balance")
    print("2. Add Money")
    print("3. Spend Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Wallet Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to add: "))

        if amount > 0:
            balance += amount
            transactions.append("Added ₹" + str(amount))
            print("Money added successfully!")
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to spend: "))

        if 0 < amount <= balance:
            balance -= amount
            transactions.append("Spent ₹" + str(amount))
            print("Payment successful!")
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == "4":
        print("\nTransaction History:")

        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions yet.")

    elif choice == "5":
        print("Thank you for using Digital Wallet!")
        break

    else:
        print("Invalid choice. Try again.")
      
