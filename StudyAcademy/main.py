
# ------------------ Write a program to check weather a number is odd/even

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even number".format(num))
# else:
#    print("{0} is Odd number".format(num))


# ---------- Write a program to check whether an age is able to voting or not
# age = int(input("Enter age : "))
# if age >= 18:
#    print("Eligible for Voting!")
# else:
#    print("Not Eligible for Voting!")

# ------- Write a program to find max between two numbers
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# if a>b:
#     print(f'{a} is a maximum number')
# else:
#     print(f'{b} is a maximum number')

# ------ Write a program to find max between three numbers
# num1 = 10
# num2 = 14
# num3 = 12
#
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3
#
# print("The largest number is", largest)

# ----- Write a program to check weather a given number is positive , negative or zero
# number = int(input("Enter any number : "))
# if number > 0:
#     print(number,"is postive number")
# elif number < 0:
#     print(number, "is negative number")
# else:
#     print(number, "is equal to zero")

# ---- Write a program to find the middle number in a group of three numbers.
# num1=int(input("Input first number: "))
# num2=int(input("Input second number: "))
# num3=int(input("Input tird number: "))
#
# if(num2>num1 and num1>num3 or num3>num1 and num1>num2):
#     print(num1, "is a middle number")
#     #check and display whether the num1 is middle
#
# if(num1>num2 and num2>num3 or num3>num2 and num2>num1):
#     print(num2, "is a middle number")
#     #check and display whether the num2 is middle
#
# if(num1>num3 and num3>num2 or num2>num3 and num3>num1):
#     print(num3, "is a middle number")
#     #check and display whether the num3 is middle

# --- Write a program to calculate total marks in 5 subjects (Full marks = 100),percentage and grade
maths = float(input("Enter maths mark : "))
chemistry = float(input("Enter chemistry mark : "))
physics = float(input("Enter physics mark : "))
english = float(input("Enter english mark : "))
computer = float(input("Enter computer mark : "))
total = maths+chemistry+physics+english+computer
percentage = (total*100)/500
print("Obtained marks : ",total)
print("percentage is : ",percentage,"%")
if percentage >= 80 and percentage <= 100:
    print("Grade : A+1 ")
elif percentage >= 70 and percentage <80:
    print("Grade : A")
elif percentage >= 60 and percentage < 70:
    print("Grade : B")
elif percentage >= 50 and percentage < 60:
    print("Grade : C")
elif percentage >= 40 and percentage < 50:
    print("Grade : D")
else:
    print("Grade :  Fail :(")



