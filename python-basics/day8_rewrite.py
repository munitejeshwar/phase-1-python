FILENAME="new.txt"

def addstudent():
    name=input()
    marks = list(map(int, input().split()))

    student={
        "name":name,
        "marks":marks
    }
    return student

def calculation(student):
    total=sum(student["marks"])
    average=total/len(student["marks"])

    if average>=40:
        result="pass"
    else:
        result="fail"
    student["total"] = total
    student["average"] = average
    student["result"] = result

    return student
def to_save(student):
    try:
        with open(FILENAME,"a") as k:
            k.write(str(student)+"\n")
        print("successfully printed the data")
    except:
        print("Error while opening")

def load_data():
    try:
        with open(FILENAME,"r") as k:
            for i in k:
                print(i.strip())
    except:
        print("Error")

student=addstudent()
student=calculation(student)


print("\nStudent Details:")
print("Name:", student["name"])
print("Marks:", student["marks"])
print("Total:", student["total"])
print("Average:", student["average"])
print("Result:", student["result"])

to_save(student)
load_data()
