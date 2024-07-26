#-------------------------------------- function define and calling
from builtins import complex
from itertools import count


def myinfo():
    print("I am learning function")

myinfo()
myinfo()
myinfo()
myinfo()
#----------------------------------------function with one argument
def country(name):
    print("my country name is :",name)
country("Pakistan")
country("france")
country("england")
#----------------------------------------function with more then one argument
def std(id,name,sub,bc):
    print("Enrollnment is :",id)
    print("Name is :", name)
    print("Subject is :", sub)
    print("Batch Code is :", bc)
std(100,"Muhammad Ahmed","Python","1812B1")

#----------------------------------------function with arbitrary argument
def student(*std):
    print("One Student in class is ", std[0])
    print("2nd Student in class is ", std[1])
    print("Third Student in class is ", std[2])
    print("Fourth Student in class is ", std[3])
    print("Last Student in class is ",std[4])

student("Anus","Tariq","Ghulam","Ali","Mehtab")

#----------------------------------------function with arbitrary argument print with loop
def student(*std):
    for i in std:
        print("Student name is :",i)

student("Anus","Tariq","Ghulam","Ali","Mehtab")
#----------------------------------------function with keywords argument
def currency(pak,ind,eng,usa):
    print("Pakistan currency is",pak)
    print("India currency is", ind)
    print("USA currency is", usa)
    print("England currency is", eng)

currency(usa="$",pak="PKR",ind="₹",eng="£")
#----------------------------------------function with keywords unknown argument
def players(**ply):
    # print("Pakistan player Babar age is ", ply["Babar"])
    # print("Indian player virat age is ",ply["Virat"])
    # print("Pakistan player Shaheen age is ", ply["Shaheen"])
    # print("Pakistan player Amir age is ", ply["Amir"])
    for i in ply:
        print("players age is ", ply[i])
players(p1="Virat 34",p2="Babar 32",p3="Amir 38",p4="Shaheen 27")
#----------------------------------------function with default argument
def set_height(value=5.6):
    print("Height is :",value)

set_height(5.7)
set_height(4.5)
set_height()