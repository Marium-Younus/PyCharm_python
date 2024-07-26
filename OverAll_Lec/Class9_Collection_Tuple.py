#=================== tuple data collection
print("--------------------------------------------------------------------------Access item in tuple")
print("---------------------------------------------------------------- +ve index")
players =("Alpha","charlie","bravo","Moin","Virat","Amir")
print(players[2])
print("---------------------------------------------------------------- -ve index")
print(players[-2])
print("---------------------------------------------------------------- via range")
print(players[2:5])
print("---------------------------------------------------------------- via start")
print(players[:3])
print("---------------------------------------------------------------- via end")
print(players[3:])
print("-----------------------------------------------------------------change item in tuple")
stationary = ("ruler","pencil","rubber","pen","sharpner")
up=list(stationary) #convert list
# print(type(up))
up[3]="beg" # change the item in list
x=tuple(up) #again convert in tuple
print(x)
print("------------------------------------------------------------------add item in tuple")
additem = list(stationary) #list
additem.append("color pencil") #add item via append ,extend,insert
additem.insert(3,"board marker")
y = tuple(additem) # convert in tuple
print(y)
print("------------------------------------------------------------------add item in tuple into tuple")
tup1=("a","b","c")
tup2=("x","y","z")
tup1 += tup2
print(tup1)
for j in tup1:
    print(j)

