
#-------------------------- Collection datatype python
print("------------------------------------------------------------------------------Learning List--------------------------")
flower=["Rose","Lilly","Lotus","Tulip","Sunflower","Daffodil","Cauliflower"]
print(flower)

#-------------------Operation on list collection datatype
print("-----------------------------------------------------------------Access Item +ve index")
print(flower[0])
print("-----------------------------------------------------------------Access Item -ve index")
print(flower[-1])
print(flower[-2])
print("-----------------------------------------------------------------Access Item via range")
print(flower[1:4])
print("-----------------------------------------------------------------Access Item via start of the list")
print(flower[:3])
print("-----------------------------------------------------------------Access Item via end of the list")
print(flower[3:])
#--------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------Change Item via index")
flower[2] = "Orchid"
print(flower)
print("-----------------------------------------------------------------Change Item via range")
flower[1:4]=["Carnation","Hyacinth","Mogra"]
print(flower)

print("-----------------------------------------------------------------Change Item via single value")
flower[1:3]=["cauliflower"]
print(flower)
#------------------------------------------------------------------------------------
print("-----------------------------------------------------------------Add Item via append function")
flower.append("Daffodil")
print(flower)
print("-----------------------------------------------------------------Add Item via insert function")
flower.insert(2,"Freesia")
print(flower)
print("-----------------------------------------------------------------Add Item via extend function")
flower2 = ["Galdiolus","Anemone"]
flower.extend(flower2)
print(flower)
print("-----------------------------------------------------------------Add Item via tuple DT")
flower3 = ("Galdiolus","Anemone")
flower.extend(flower3)
print(flower)
#------------------------------------------------------------------------------------
print("-----------------------------------------------------------------Remove Item via remove function")
flower.remove("Lilly")
print(flower)
print("-----------------------------------------------------------------Remove Item via pop function")
flower.pop(3)
print(flower)
print("-----------------------------------------------------------------Remove Item via pop function")
flower.pop()
print(flower)
print("-----------------------------------------------------------------Remove Item via del keyword")
del flower[2]
print(flower)
print("-----------------------------------------------------------------Remove Item via clear function")
flower.clear()
print(flower)
print("-----------------------------------------------------------------Delete whole variable via del keyword")
del flower
print("Whole list is deleted")

#----------------------------------*********************************************----------------------------
# ----------------------------------*********************************************----------------------------
# ----------------------------------*********************************************----------------------------
# ----------------------------------*********************************************----------------------------

#-------------------- list collection via loop
print("--------------------------------------------------------------------------List collection via Loop")
student = ["Muhammad Ali","Muhammad Ahmed","Saad","Mahad","Sara","Moiz","Bilal"];
for i in student:
    print(i)
print("--------------------------------------------------------------List collection via range and len method")
for x in range(len(student)):
    print(student[x])
# --------------------------------- list collection via sort
print("--------------------------------------------------------------List collection via sort")
student.sort(reverse=True)
print(student)
for j in student:
    print(j)

percentage = [89.5,66.78,45.56,90.2,79.9] #acs
percentage.sort(reverse=True)
print(percentage)
for per in percentage:
    print(per)
#--------------------------------- list collection via copy
print("---------------------------------------------------------------List collection via copy method")
person =student.copy();
print(person)
for k in person:
    print(k)
print("----------------------------------------------------------------List collection via list method")
employee = list(student)
print(employee)
for a in employee:
    print(a)
#--------------------------------- list collection via join
print("----------------------------------------------------------------Add two list")
mobile = ["Samsung","Nokia","iphone"]
model =[2019,2020,2008]
result = mobile+model
print(result)
for m in result:
    print(m)
print("----------------------------------------------------------------Join via append method")
mobile.append(model)
print(mobile)
for n in mobile:
    print(n)
print("----------------------------------------------------------------Join via extend method")
mobile.extend(model)
print(mobile)
for o in mobile:
    print(o)