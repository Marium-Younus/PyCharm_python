print("---------------------------------------------read()")
# f = open("student.txt", "r")
# data1 = f.read(3)
# data2 = f.read()
# print(data1)
# print(data2)
# f.close()

print("---------------------------------------------readline()")
# f = open("student.txt", "r")
# data1 = f.readline()
# data2 = f.readline()
# print(data1,end="")
# print(data2,end="")
# f.close()
print("---------------------------------------------readlines()")
f = open("student.txt", "r")
data1 = f.readlines()
for line in data1:
    print(line)
f.close()


