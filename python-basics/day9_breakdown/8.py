students = {}

with open("students.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")

        sid = int(parts[0])
        name = parts[1]
        marks = list(map(int, parts[2:]))

        students[sid] = {
            "name": name,
            "marks": marks
        }

print(students)
