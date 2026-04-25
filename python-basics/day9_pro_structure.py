# copy-paste:

FILE_NAME = "student.txt"


def load_students():
    try:
        with open(FILE_NAME) as f:
            return {
                int(p[0]): {
                    "name": p[1],
                    "marks": list(map(int, p[2:]))
                }
                for p in (line.strip().split(",") for line in f)
            }
    except FileNotFoundError:
        return {}


def save_students(students):
    with open(FILE_NAME, "w") as f:
        for sid, d in students.items():
            f.write(f"{sid},{d['name']}," +
                    ",".join(map(str, d["marks"])) + "\n")


def get_next_id(students):
    return max(students, default=0) + 1


def add_student(students):
    students[get_next_id(students)] = {
        "name": input("Enter name: "),
        "marks": list(map(int, input("Enter marks: ").split()))
    }


def update_student(students):
    sid = int(input("Enter ID to update: "))
    if sid in students:
        students[sid]["marks"] = list(map(int, input("Enter new marks: ").split()))
    else:
        print("Invalid ID")


def delete_student(students):
    if students.pop(int(input("Enter ID to delete: ")), None) is None:
        print("Invalid ID")


def view_students(students):
    if not students:
        return print("No students found")

    for sid, d in students.items():
        avg = sum(d["marks"]) / len(d["marks"])
        print(f"ID:{sid} Name:{d['name']} "
              f"Marks:{d['marks']} Avg:{avg:.2f} "
              f"{'Pass' if avg >= 40 else 'Fail'}")


def main():
    students = load_students()

    actions = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": view_students
    }

    while True:
        print("\n1.Add 2.Update 3.Delete 4.View 5.Exit")
        choice = input("Choose: ")

        if choice == "5":
            break

        action = actions.get(choice)
        if action:
            action(students)
            if choice != "4":
                save_students(students)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
