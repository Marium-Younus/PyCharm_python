# working with while loop
# i=1 #initialize
# while i<11: #condition
#     print("The value of i is ",i)
#     i += 1 # inc/dec
#----------------------------------------Dec order via while loop
# j=10
# while j>=1:
#     print("The value if j is :" ,j)
#     j -= 1
#----------------------------------------write to take input from user and print table
# table = int(input("Enter any number : "));
# k=1
# while k<=10:
#     print(table," * ",k," = ",(table*k))
#     k += 1
#---------------Working with nested while loop
# r=1
# while r<=3:
#     print("The R outer is : ------------------- ",r)
#     c=1
#     while c<=3:
#         print("The C inner is : ",c)
#         c+=1
#     r+=1
#---------------Working with for loop in python
# player = ["Babar Azam","Virat Kholi","Muhmmad Rizwan","Muhammad Amir","Shaheen Shah Afridi"]
# for ply in player:
#     print(ply)
#---------------Working with looping through a string
# for fruits in "banana":
#     print(fruits)
#---------------Working with looping break Statement
# friuty = ["apple","banana","cherry"]
# for ft in friuty:
#     if ft == "banana":
#         continue
#     print(ft)
#---------------Working with for loop with range function
# for a in range(10):
#     print(a)
# # ---------------Working with  for loop with range function via start and end
# for b in range(3,7):
#     print(b)
# # ---------------Working with for loop with range function via increase in our own wish
# for c in range(0,50,20):
#     print(c)
#---------------Working with Nested for loop
country= ["India","Pakistan","England"]
fruits =["apple","pineapple","grapes"]
for row in country:
    for col in fruits:
        print(row,col)