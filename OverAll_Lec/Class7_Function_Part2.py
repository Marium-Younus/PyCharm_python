
#------------------------------------------ function via list
# def country(mylist):
#     for x in mylist:
#         print(x)
# con = ["Pakistan","England","Canada","UAE","India"] #list
# player=("Amir","John","Kelvin","Muhammad ali","Virat") #tuple
# country(con)
# country(player)

#------------------------------------------ function via return value
def arithematic(i,j):
    k=i*j
    return k
    print("the mul result is ",arithematic(5,5))


#------------------------------------------ function arg Arbitrary via return value
def myfunct(*a):
    b = sum(a)

    return b
print("the sum result is ",myfunct(4,3,6,90,87,65))

#------------------------------------------ function recursion via factorial
num = int(input("Enter any number : "))
def fact(y):
    if y == 1:
        return 1
    else:
        return y * fact(y-1) #recursion

print("The factorial of given number ",num ,"is : ",fact(num))