try:
    with open("students.txt", "r") as f:
        for line in f:
            print(line.strip())
except:
    print("File not found")


# FILE_NAME = "students.txt"


# def add_student():
#     name = input("Enter student name: ")

#     print("Enter marks for 3 subjects (space separated):")
#     marks = list(map(int, input().split()))

#     student = {
#         "name": name,
#         "marks": marks
#     }
#     return student


# def calculate_result(student):
#     total = sum(student["marks"])
#     average = total / len(student["marks"])

#     if average >= 40:
#         result = "Pass"
#     else:
#         result = "Fail"

#     student["total"] = total
#     student["average"] = average
#     student["result"] = result

#     return student


# def save_to_file(student):
#     try:
#         with open(FILE_NAME, "a") as f:
#             f.write(str(student) + "\n")
#         print("Student data saved successfully.")
#     except Exception as e:
#         print("Error while saving to file:", e)


# def load_from_file():
#     try:
#         with open(FILE_NAME, "r") as f:
#             print("\nLoaded Records:")
#             for line in f:
#                 print(line.strip())
#     except FileNotFoundError:
#         print("No records found. File does not exist.")
#     except Exception as e:
#         print("Error while reading file:", e)


# student = add_student()
# student = calculate_result(student)

# print("\nStudent Details:")
# print("Name:", student["name"])
# print("Marks:", student["marks"])
# print("Total:", student["total"])
# print("Average:", student["average"])
# print("Result:", student["result"])

# save_to_file(student)
# load_from_file()
