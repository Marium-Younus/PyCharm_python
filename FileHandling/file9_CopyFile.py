f1 = open("student.txt", mode="r",encoding="UTF-8")
f2 = open("person.txt", mode="w",encoding="UTF-8")
for line in f1:
    f2.write(line)
f1.close()
f2.close()

