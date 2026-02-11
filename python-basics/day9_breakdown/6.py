sid = 1
name = "Teja"
marks = [60, 70, 80]

line = str(sid) + "," + name + "," + ",".join(map(str, marks))

with open("students.txt", "a") as f:
    f.write(line + "\n")
