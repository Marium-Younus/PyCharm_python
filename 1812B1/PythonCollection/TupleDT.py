#=================== tuple data collection
# print("---------Access item in tuple")
# print("-------------- +ve index")
# players =("Alpha","charlie","bravo","Moin","Virat","Amir")
# print(players[2])
# print("-------------- -ve index")
# print(players[-2])
# print("-------------- via range")
# print(players[2:5])
# print("-------------- via start")
# print(players[:3])
# print("-------------- via end")
# print(players[3:])
# print("---------change item in tuple")
# stationary = ("ruler","pencil","rubber","pen","sharpner")
# up=list(stationary) #convert list
# # print(type(up))
# up[3]="beg" # change the item in list
# x=tuple(up) #again convert in tuple
# print(x)
# print("---------add item in tuple")
# additem = list(stationary) #list
# additem.append("color pencil") #add item via append ,extend,insert
# additem.insert(3,"board marker")
# y = tuple(additem) # convert in tuple
# print(y)
# print("---------add item in tuple into tuple")
# tup1=("a","b","c")
# tup2=("x","y","z")
# tup1 += tup2
# print(tup1)
# for j in tup1:
#     print(j)
# print("---------unpack tuple")
# currency =("PKR","Euro","Pound","Dollar") #packing tuple
# (Pakistan,Brazil,United_Kingdom,America) = currency #unpack tuple
# print("Pakistan Currency is",Pakistan)
# print("Brazil Currency is",Brazil)
# print("England Currency is",United_Kingdom)
# print("USA Currency is",America)
#
# print("---------Asterisk* tuple")
student = ("Ali 5.4","Waleed 5.6","Anas 5.8","Waqas 5.5","Shifa 5.5","Mehtab 5.5","Ghulam 5.5","Tariq 5.7","Umar 5.6")
# (Ali,Waleed,Anas,*Same,Tariq,Umar)=student
# print(Ali)
# print(Waleed)
# print(Anas)
# print(Same)
# print(Tariq)
# print(Umar)

print("---------for loop using in tuple")
for std in student:
    print(std)
print("---------for loop using index in tuple")
for x in range(len(student)):
    print(student[x])

print("---------while loop in tuple")
j=0
while j<len(student):
    print(student[j])
    j=j+1
























