# f = open("not_exist.txt", "r")


# to stop error

try:
    f = open("nofile.txt", "r")
except:
    print("File not found")
