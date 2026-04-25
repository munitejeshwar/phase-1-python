students = {}

while True:
    print("1. Add")
    print("2. View")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        marks = list(map(int, input("Marks: ").split()))
        students[len(students)+1] = {"name": name, "marks": marks}

    elif choice == "2":
        print(students)

    elif choice == "3":
        break