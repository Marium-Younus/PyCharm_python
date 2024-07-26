#--- Write a program to print first 10 natural number.
# print("====The First 10 Natural Numbers====")
# i = 1
# while(i <= 10):
#     print(i)
#     i = i + 1

# ---- Write a program to print first N natural number
# num=int(input("Please enter maxinmum number: "))
# print("Natural numbers 1 to ",num )
# for i in range(1,num+1):
#      print(i)
# --- Write a program to print first N natural number in reverse order.
#
# number = int(input("Please Enter any Number: "))
# i = number
# print("List of Natural Numbers from {0} to 1 in Reverse Order : ".format(number))
# while ( i >= 1):
#     print (i, end = '  ')
#     i = i - 1

# --- Write a program to find sum of first n natural numbers.
# num = int(input("Please Enter any Number: "))
# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    # use while loop to iterate until zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)

# --- Write a program to find sum of square of first n natural numbers
n = int(input("Enter nth number : "))
sum = 0
while n>0:
    sum = sum + (n*n)
    n = n-1
print("sum of squares is : ",sum)

