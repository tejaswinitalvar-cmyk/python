# Library Management System using python programming language 

books = {}

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")

        if name in books:
            books[name] += 1
        else:
            books[name] = 1

        print("Book added successfully!")

    elif choice == "2":
        if books:
            for name, quantity in books.items():
                print(name, "- Available:", quantity)
        else:
            print("No books available.")

    elif choice == "3":
        name = input("Enter book name to issue: ")

        if name in books and books[name] > 0:
            books[name] -= 1
            print("Book issued successfully!")
        else:
            print("Book not available.")

    elif choice == "4":
        name = input("Enter book name to return: ")

        if name in books:
            books[name] += 1
            print("Book returned successfully!")
        else:
            print("Book not found in library.")

    elif choice == "5":
        print("Thank you for using the library system!")
        break

    else:
        print("Invalid choice. Try again.")
      
