import os
if os.path.isfile("student.txt"):
    print("File exist")
    f = open("student.txt", "r")
    print(f.read())
    f.close()
else:
    print("File not exist")


