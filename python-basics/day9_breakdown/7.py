with open("students.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print(parts)
