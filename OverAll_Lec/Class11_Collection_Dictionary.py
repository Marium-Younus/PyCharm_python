print("------------------------------------------------------------------------We are talking about dictionary data type")
car = {
            "model":"Toyota",
            "make":"Ceria",
            "year":2019
        }
print(car)
print("---------------------------------------------------------------------------------------------working with operations")
print("1.----------------------------------------> Access Item via key")
print("Car Model is :",car["model"])
print("Car Make is :",car["make"])
print("Car year is :",car["year"])
print("1.----------------------------------------> Access Item via get method")
print("Car Model is :",car.get("model"))
print("Car Model is :",car.get("make"))
print("Car Model is :",car.get("year"))
print("1.----------------------------------------> Access Item via check key if exist")
x=car.keys()
# print(x)
for i in x:
    # print(i)
    if "make" in i:
        print(i,"key is present in the car dictionary")
        break
else:
    print("no its not present")
print("1.----------------------------------------> Access Item via check key if exist another way")
str = "model"
if str in car:
    print(str,"key is present in the car dictionary")
else:
    print(str,"key is not present in the car dictionary")

print("2.---------------- change item via key")
car["year"] =2022
print(car)
print("2.---------------- change item via update method")
car.update({"model":"honda"})
print(car)
print("3.---------------- add item via key")
car["color"] ="black"
print(car)
print("3.---------------- add item via update method")
car.update({"xyz":"bla bla"})
print(car)
print("4.---------------- remove item pop")
car.pop("xyz")
print(car)
print("4.---------------- remove item popitem")
car.popitem()
print(car)
print("4.---------------- empty via clear")
car.clear()
print(car)
print("4.---------------- delete via del")
del car
print("car deleted")