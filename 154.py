# To-Do List Manager using python programming language 

tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['name']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Try again.")
      
  
