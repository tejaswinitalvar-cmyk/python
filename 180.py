# Shopping Discount Calculator using python programming language

print("Welcome to Discount Calculator!")

price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

if price >= 0 and 0 <= discount <= 100:
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    print("\n--- Discount Report ---")
    print("Original Price: Rs.", price)
    print("Discount:", discount, "%")
    print("Discount Amount: Rs.", discount_amount)
    print("Final Price: Rs.", final_price)
else:
    print("Please enter valid values!")
