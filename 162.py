# Hotel Room Booking System using python programming language 

rooms = {
    101: {"type": "Single", "price": 1000, "available": True},
    102: {"type": "Double", "price": 2000, "available": True},
    103: {"type": "Deluxe", "price": 3000, "available": True},
    104: {"type": "Suite", "price": 5000, "available": True}
}

while True:
    print("\n===== HOTEL BOOKING SYSTEM =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for number, room in rooms.items():
            status = "Available" if room["available"] else "Booked"
            print(number, "-", room["type"],
                  "- ₹", room["price"], "-", status)

    elif choice == "2":
        number = int(input("Enter room number: "))

        if number in rooms and rooms[number]["available"]:
            days = int(input("Enter number of days: "))

            if days > 0:
                total = rooms[number]["price"] * days
                rooms[number]["available"] = False

                print("Room booked successfully!")
                print("Total amount: ₹", total)
            else:
                print("Days must be positive.")
        else:
            print("Room not available.")

    elif choice == "3":
        number = int(input("Enter room number: "))

        if number in rooms and not rooms[number]["available"]:
            rooms[number]["available"] = True
            print("Booking cancelled successfully!")
        else:
            print("No booking found.")

    elif choice == "4":
        print("Thank you for using Hotel Booking System!")
        break

    else:
        print("Invalid choice. Try again.")
      
