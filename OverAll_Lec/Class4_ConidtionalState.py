#--------------------------------------------------------------------------------------------------------------------------------
print("Q1.Write a program to check weather a number is odd/even.")
num1 = int(input("Enter any number : "))
if num1%2==0:
    print(num1," is even number")
else:
    print(num1, " is odd even number")
#--------------------------------------------------------------------------------------------------------------------------------
print("Q2.Write a program to check weather an age is able to voting or not.")
age = int(input("Enter your age: "))
if age>=18:
    print("Your are eligible for casting a vote because your age is ",age)
else:
    print("Your are not eligible for casting a vote because your age is ", age)
#--------------------------------------------------------------------------------------------------------------------------------
print("Q3.Write a program to find max between two numbers.")
number1 = int(input("Enter 1st Number: "))
number2 = int(input("Enter 2nd Number: "))

if number1 > number2:
    print(number1,number2,"Max number is:",number1)
else:
    print(number1,number2,"Max number is:",number2)
#--------------------------------------------------------------------------------------------------------------------------------
print("Q4 Write a program to find max between three numbers.")
a = int(input("Enter 1st Number: "))
b= int(input("Enter 2nd Number: "))
c = int(input("Enter 1st Number: "))
if a>b and a>c:
    print(a," ",b," ",c," ","max number is ",a)
elif b>a and b>c:
    print(a," ",b," ",c," ","max number is ",b)
else:
    print(a, " ", b, " ", c, " ", "max number is ", c)
#--------------------------------------------------------------------------------------------------------------------------------
print("Q5.Write a program to check weather a given number is positive , negative or zero.")
x=int(input("Enter any Number: "))
if x>0:
    print(x," is postive number")
elif x<0:
    print(x," is negative number")
else :
    print("Zero number")
#--------------------------------------------------------------------------------------------------------------------------------
print("Q6.Write a program to find the middle number in a group of three numbers.")
i = int(input("Enter 1st Number: "))
j = int(input("Enter 2nd Number: "))
k = int(input("Enter 1st Number: "))
if (i>j and i<k) or (i<j and i>k):
    print("Middle number is :",i)
elif (j>i and j<k) or (j<i and j>k):
    print("Middle number is :",j)
else:
    print("Middle number is :", k)
#--------------------------------------------------------------------------------------------------------------------------------
print("Q7.Write a program to calculate total marks in 5 subjects  as well as percentage of marks and find its grade .")
eng=int(input("Enter English Marks : "))
math=int(input("Enter Maths Marks: "))
urdu=int(input("Enter Urdu Marks: "))
phy=int(input("Enter Physics Marks: "))
chem=int(input("Enter Chemistry Marks: "))
total = eng+math+urdu+phy+chem;
percentage= total*100/500;
print("Obtained marks is : ",total)
print("Percentage is : ",percentage,"%")
if percentage>=80 and percentage<=100:
    print("Grade is A+1 😊")
elif percentage>=70 and percentage<80:
    print("Grade is A 😊")
elif percentage>=60 and percentage<70:
    print("Grade is B 😐 ")
elif percentage>=50 and percentage<60:
    print("Grade is C 😐 ")
elif percentage>=40 and percentage<50:
    print("Grade is D 😐 ")
else:
    print("Fail 🙁")