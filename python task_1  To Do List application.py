tasks = []

while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '3':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed.")
        else:
            print("Invalid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Please enter a valid choice.")
