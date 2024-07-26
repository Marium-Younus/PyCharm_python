#--------------------------------------------------------------------------------------------------------------------------------
print("Q1.Write a program to print first 10 natural number.")
i=1
while i<=10:
    print("natural number is:",i)
    i=i+1
#--------------------------------------------------------------------------------------------------------------------------------
print("Q2.Write a program to print first N natural number.")
num= int(input("Enter any Number: "))
i=1
while i<=num:
    print("natural number is:",i)
    i=i+1
#--------------------------------------------------------------------------------------------------------------------------------
print("Q3.Write a program to print first N natural number in reverse order")
n1= int(input("Enter any Number: "))
while n1>=1:
    print("natural number is:",n1)
    n1=n1-1
#--------------------------------------------------------------------------------------------------------------------------------
print("Q4.Write a program to find sum of first n natural numbers.")
x= int(input("Enter any Number: "))
i=1
sum=0
while i<=x:
    print("natural number is:",i)
    sum=sum+i
    i=i+1
print("Sum of first n natural numbers. is",sum )
#--------------------------------------------------------------------------------------------------------------------------------
print("Q5.Write a program to find sum of square of first n natural numbers.")

#-----------------------------------****************** Programs Level 2 ***************------------------------------------------
print("Q1.Write a program to print factorial of a given number.")
number = int(input("Enter any Number: "))
fact = 1
while(number>0):
    fact=fact*number
    number=number-1
    # print("Number ", number)
print("Factorial of a given number is ",fact )
#----------------------------------------------------------------------------------------------------------------------------------
print("Q2.Write a program to check whether a given number is Armstrong or not.")
n1 = int(input("Enter any Number: "))
orig = n1
sum=0
while(n1>0):
    sum= sum+(n1%10)*(n1%10)*(n1%10)
    n1=n1//10
if orig == sum:
    print(orig,"is an Armstrong number")
else:
    print(orig, "is not an Armstrong number")
#----------------------------------------------------------------------------------------------------------------------------------
print("Q3.Write a program to check whether a given number is palindrome or not.")
n2 = int(input("Enter any Number: "))
rev=0
temp=n2
while(n2>0):
    rev= (rev*10)+n2%10
    n2 = n2 // 10
if temp == rev:
    print(temp,"is a palindrome number")
else:
    print(temp, "is not a palindrome number")
#----------------------------------------------------------------------------------------------------------------------------------
print("Q4.Write a program to print Fibonacci series upto a given number.")
n3 = int(input("Enter any Number: "))
m=0
n=1
o=0
while(o<=n3):
    print(o)
    m=n
    n=o
    o=m+n
#----------------------------------------------------------------------------------------------------------------------------------
print("Q5.Write a program to printing Stars '*' in Right Angle Triangle Shape.")
row=1
while(row<=5):
    col=1
    while(col<=row):
        print("*",end=' ')
        col=col+1
    print()
    row=row+1