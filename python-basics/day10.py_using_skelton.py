FILE_NAME = "data.txt"

def load_data():
    # read file and return data
    pass

def save_data(data):
    # write file
    pass

def add_item(data):
    pass

def update_item(data):
    pass

def delete_item(data):
    pass

def display(data):
    pass

def main():
    data = load_data()

    while True:
        print("\n1. Add")
        print("2. Update")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item(data)
        elif choice == "2":
            update_item(data)
        elif choice == "3":
            delete_item(data)
        elif choice == "4":
            display(data)
        elif choice == "5":
            save_data(data)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
