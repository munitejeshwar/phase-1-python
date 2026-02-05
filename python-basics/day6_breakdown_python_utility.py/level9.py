student = "Teja"

with open("students.txt", "a") as f:
    f.write(str(student) + "\n")
