# Today we are talk about print() and input() function
print("Hello World")
#--------------------------------------more than one object
#---------------------------------------------==========================-print()-==========================----------------------
print("Hello","How are You?")
a=10
b=20
c=a+b
s=a-b
m=a*b
d=a/b
print("Addition of ",a,"+",b,"=",c)
print("Subtraction of ",a,"-",b,"=",s)
print("Multiplication of ",a,"*",b,"=",m)
print("Division of ",a,"/",b,"=",d)
#--------------------------------------------print as a tuple
x=("Apple","Mango","Banana")
print(x)
#--------------------------------------------specify the seperator
print("Good","Bye",sep="---")

#---------------------------------------------==========================-input()-==========================----------------------
print("Enter your name: ")
x = input()
print("My name is ",x)

y = input("What is your country name : ")
print("Country is ",y)
#--------==========================-arithematic operation via input()==========================----------------------
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter 2nd Number : "))
result = num1+num2
print("The Add Result is :",result)
#============================
x, y, z = 10,67,67
print(x," ",y," ",z)
