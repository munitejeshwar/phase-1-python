# copy-paste:
FILE_NAME = "student.txt"


def load_students():
    students = {}
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                sid = int(parts[0])
                name = parts[1]
                marks = list(map(int, parts[2:]))
                students[sid] = {"name": name, "marks": marks}
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(FILE_NAME, "w") as f:
        for sid, data in students.items():
            line = f"{sid},{data['name']}," + ",".join(map(str, data["marks"]))
            f.write(line + "\n")


def get_next_id(students):
    if not students:
        return 1
    return max(students.keys()) + 1


def add_student(students):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    sid = get_next_id(students)
    students[sid] = {"name": name, "marks": marks}
    print(f"Student added with ID {sid}")


def update_student(students):
    sid = int(input("Enter student ID to update: "))
    if sid not in students:
        print("Invalid ID")
        return
    marks = list(map(int, input("Enter new marks: ").split()))
    students[sid]["marks"] = marks
    print("Student updated")


def delete_student(students):
    sid = int(input("Enter student ID to delete: "))
    if sid in students:
        del students[sid]
        print("Student deleted")
    else:
        print("Invalid ID")


def view_students(students):
    if not students:
        print("No students found")
        return

    for sid, data in students.items():
        total = sum(data["marks"])
        avg = total / len(data["marks"])
        result = "Pass" if avg >= 40 else "Fail"
        print(f"ID:{sid} Name:{data['name']} Marks:{data['marks']} Avg:{avg:.2f} {result}")


def main():
    students = load_students()

    while True:
        print("\n1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View students")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            update_student(students)
            save_students(students)
        elif choice == "3":
            delete_student(students)
            save_students(students)
        elif choice == "4":
            view_students(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
