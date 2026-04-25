student = {
    "name": "Teja",
    "marks": [60, 70, 80]
}

with open("students.txt", "a") as f:
    f.write(str(student) + "\n")
