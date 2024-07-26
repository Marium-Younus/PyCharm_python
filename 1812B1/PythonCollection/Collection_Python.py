#-------------------- list collection via loop
print("--------------list collection via loop")
student = ["Muhammad Ali","Muhammad Ahmed","Saad","Mahad","Sara","Moiz","Bilal"];
# for i in student:
#     print(i)
# print("--------------list collection via range and len method")
# for x in range(len(student)):
#     print(student[x])
#--------------------------------- list collection via sort
# print("-------------- list collection via sort")
# student.sort(reverse=True)
# print(student)
# for j in student:
#     print(j)
#
# percentage = [89.5,66.78,45.56,90.2,79.9] #acs
# percentage.sort(reverse=True)
# print(percentage)
# for per in percentage:
#     print(per)
#--------------------------------- list collection via copy
print("---------------------list collection via copy method")
person =student.copy();
print(person)
for k in person:
    print(k)
print("---------------------list collection via list method")
employee = list(student)
print(employee)
for a in employee:
    print(a)
#--------------------------------- list collection via join
print("-------------------- add two list")
mobile = ["Samsung","Nokia","iphone"]
model =[2019,2020,2008]
result = mobile+model
print(result)
for m in result:
    print(m)
print("-------------------- join append method")
mobile.append(model)
print(mobile)
for n in mobile:
    print(n)
print("-------------------- join extend method")
mobile.extend(model)
print(mobile)
for o in mobile:
    print(o)