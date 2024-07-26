print("Learning Set Datatype for python collection")
color={"Red","Green","Blue","Purple","Pink","Orange","Grey","Magenta","Silver","Gold"} #set color variable store
# print("1----Access set values")
# for x in color:
#     print(x)
# print("1-------Check if puple is present in the set or not")
# print("Purple" in color)
#
# print("2----Add item in set ")
# color.add("Black")
# for x in color:
#     print(x)
# print("2----Add item using update in set ")
# colour = {"white","indigo","maroon","grey","yellow"}
# color.update(colour)
# for j in color:
#     print(j)
# print("2----Add item using iterable object ")
# mobile = {"Nokia","iphone","Samsung","Oppo"} #set
# year =[2002,2030,2019,2021] #list iterable object
# mobile.update(year)
# for i in mobile:
#     print(i)
print("3----Remove item in set ")
color.remove("Magenta")
for x in color:
    print(x)
print("3----discard item in set ")
color.discard("Silver")
for x in color:
    print(x)
print("3----pop item in set to remove last value")
y=color.pop();
print(y)
print("----------------------------")
for x in color:
    print(x)
print("3----clear item in set ")
color.clear()
print(color)
print("3----del item in set ")
del color
