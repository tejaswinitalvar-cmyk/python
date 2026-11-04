# Shopping Cart System using python programming language 

products = {
    "Laptop": 50000,
    "Phone": 20000,
    "Headphones": 1500,
    "Mouse": 800
}

cart = {}

while True:
    print("\n===== SHOPPING CART =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for name, price in products.items():
            print(name, "- ₹", price)

    elif choice == "2":
        name = input("Enter product name: ")

        if name in products:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart[name] = cart.get(name, 0) + quantity
                print("Product added successfully!")
            else:
                print("Quantity must be positive.")
        else:
            print("Product not found.")

    elif choice == "3":
        if cart:
            for name, quantity in cart.items():
                print(name, "x", quantity,
                      "- ₹", products[name] * quantity)
        else:
            print("Cart is empty.")

    elif choice == "4":
        total = sum(products[name] * quantity
                    for name, quantity in cart.items())

        print("Total Bill: ₹", total)

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again.")
      
