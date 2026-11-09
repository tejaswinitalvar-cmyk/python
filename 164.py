# Food Ordering System using python programming language 

menu = {
    "1": {"name": "Pizza", "price": 250},
    "2": {"name": "Burger", "price": 120},
    "3": {"name": "Dosa", "price": 80},
    "4": {"name": "Biryani", "price": 180},
    "5": {"name": "Ice Cream", "price": 60}
}

cart = {}

while True:
    print("\n===== FOOD ORDERING SYSTEM =====")
    print("1. View Menu")
    print("2. Order Food")
    print("3. View Cart")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for item_id, item in menu.items():
            print(item_id, item["name"], "- ₹", item["price"])

    elif choice == "2":
        item_id = input("Enter food item number: ")

        if item_id in menu:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart[item_id] = cart.get(item_id, 0) + quantity
                print("Food added to cart!")
            else:
                print("Quantity must be positive.")
        else:
            print("Invalid food item.")

    elif choice == "3":
        if cart:
            for item_id, quantity in cart.items():
                item = menu[item_id]
                subtotal = item["price"] * quantity

                print(item["name"], "x", quantity,
                      "- ₹", subtotal)
        else:
            print("Your cart is empty.")

    elif choice == "4":
        total = sum(menu[item_id]["price"] * quantity
                    for item_id, quantity in cart.items())

        print("\n===== FINAL BILL =====")
        print("Total Amount: ₹", total)
        print("Thank you for ordering!")

    elif choice == "5":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice. Try again.")
      
