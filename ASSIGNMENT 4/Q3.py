def menu_driven_op():
    lst = []
    while True:
        print("\nMenu:")
        print("1. Create a list of N integers")
        print("2. Display the list elements")
        print("3. Insert an element at a specific position")
        print("4. Delete an element at a given position")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            N = int(input("Enter the number of elements: "))
            lst = [int(input(f"Enter element {_ + 1}: ")) for _ in range(N)]
        elif ch == 2:
            print(f"List: {lst}")
        elif ch == 3:
            element = int(input("Enter the element to insert: "))
            position = int(input("Enter the position: "))
            if 0 <= position <= len(lst):
                lst.insert(position, element)
            else:
                print("Invalid position.")
        elif ch == 4:
            position = int(input("Enter the position to delete: "))
            if 0 <= position < len(lst):
                lst.pop(position)
            else:
                print("Invalid position.")
        elif ch == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

menu_driven_op()
