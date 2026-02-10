# def student_marks_manager():

#     name=input("Enter Name: ")
#     print("Student Name:",name)

#     Eng_marks=int(input())
#     Tel_marks=int(input())
#     Mat_marks=int(input())

#     print("Marks:",Eng_marks,Tel_marks,Mat_marks)

#     total=Tel_marks+Eng_marks+Mat_marks
#     print("Total",total)

#     Avg=total/3
#     print("Average marks",Avg)

#     if Avg>=40:
#         print("Result:Pass")
#     else:
#         print("Result:Fail")
# student_marks_manager()
FILE_NAME = "students.txt"


def add_student():
    name = input("Enter student name: ")

    print("Enter marks for 3 subjects (space separated):")
    marks = list(map(int, input().split()))

    student = {
        "name": name,
        "marks": marks
    }
    return student


def calculate_result(student):
    total = sum(student["marks"])
    average = total / len(student["marks"])

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    student["total"] = total
    student["average"] = average
    student["result"] = result

    return student


def save_to_file(student):
    try:
        with open(FILE_NAME, "a") as k:
            k.write(str(student) + "\n")
        print("Student data saved successfully.")
    except Exception as e:
        print("Error while saving to file:", e)


def load_from_file():
    try:

        with open(FILE_NAME, "r") as k:
            print("\nLoaded Records:")
            for line in k:
                print(line.strip())
    except FileNotFoundError:
        print("No records found. File does not exist.")
    except Exception as e:
        print("Error while reading file:", e)


student = add_student()
student = calculate_result(student)

print("\nStudent Details:")
print("Name:", student["name"])
print("Marks:", student["marks"])
print("Total:", student["total"])
print("Average:", student["average"])
print("Result:", student["result"])

save_to_file(student)
load_from_file()
