while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Add Book")
    elif choice == "2":
        print("Borrow Book")
    elif choice == "3":
        print("Return Book")
    elif choice == "4":
        print("Show Books")
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice")