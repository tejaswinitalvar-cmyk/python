# Bus Ticket Reservation System using python programming language 

buses = {
    "1": {"route": "Bangalore to Mysore", "price": 300, "seats": 5},
    "2": {"route": "Bangalore to Chennai", "price": 600, "seats": 5},
    "3": {"route": "Bangalore to Hyderabad", "price": 800, "seats": 5}
}

while True:
    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. View Buses")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for bus_id, bus in buses.items():
            print(bus_id, bus["route"],
                  "- ₹", bus["price"],
                  "- Available seats:", bus["seats"])

    elif choice == "2":
        bus_id = input("Enter bus number: ")

        if bus_id in buses:
            bus = buses[bus_id]
            seats = int(input("Enter number of seats: "))

            if 0 < seats <= bus["seats"]:
                total = seats * bus["price"]
                bus["seats"] -= seats

                print("\nBooking successful!")
                print("Route:", bus["route"])
                print("Seats booked:", seats)
                print("Total amount: ₹", total)
            else:
                print("Invalid number of seats.")
        else:
            print("Bus not found.")

    elif choice == "3":
        print("Thank you for using Bus Reservation System!")
        break

    else:
        print("Invalid choice. Try again.")
      
