def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
            print("Item added successfully")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("PLease enter the name of the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print("Item removed successfully")
            else:
                print("Sorry! the item you entered is not in the list")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                for item in shopping_list:
                    print(item)
            else:
                print("Sorry the List is empty Please add an item!!")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

