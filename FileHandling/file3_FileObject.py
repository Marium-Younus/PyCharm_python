f = open("student.txt", mode="r", encoding="utf-8")
print("Name of file is ",f.name)
print("Encoding is ",f.encoding)
print("Mode of file is ",f.mode)
print("Is file close ",f.closed)
f.close()
print("Is file close ",f.closed)