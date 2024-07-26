#-----------------------using text mode
f = open("student.txt", "r")
data = f.read()
print(data)
f.close()
#-----------------------using binary mode
f = open("student.txt", "rb")
data = f.read()
print(data)
f.close()

