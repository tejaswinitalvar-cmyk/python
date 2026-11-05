# Movie Ticket Booking System using python programming language 

movies = {
    "1": {"name": "Avatar", "price": 250, "seats": 50},
    "2": {"name": "KGF", "price": 200, "seats": 40},
    "3": {"name": "Kantara", "price": 180, "seats": 30}
}

while True:
    print("\n===== MOVIE TICKET BOOKING =====")
    print("1. View Movies")
    print("2. Book Tickets")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for key, movie in movies.items():
            print(key, movie["name"],
                  "- ₹", movie["price"],
                  "- Available seats:", movie["seats"])

    elif choice == "2":
        movie_id = input("Enter movie number: ")

        if movie_id in movies:
            movie = movies[movie_id]
            tickets = int(input("Enter number of tickets: "))

            if 0 < tickets <= movie["seats"]:
                total = tickets * movie["price"]
                movie["seats"] -= tickets

                print("Booking successful!")
                print("Movie:", movie["name"])
                print("Tickets:", tickets)
                print("Total amount: ₹", total)
            else:
                print("Invalid ticket count or insufficient seats.")
        else:
            print("Movie not found.")

    elif choice == "3":
        print("Thank you for booking!")
        break

    else:
        print("Invalid choice. Try again.")
      
