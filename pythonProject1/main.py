
# Function definition to check validity
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Function definition for type
def type_of_triangle(a,b,c):
    if a==b and b==c:
        print('Acute.')
    elif a==b or b==c or a==c:
        print('Right')
    else:
        print('Obtuse')

# Reading Three Sides
side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))
side_c = float(input('Enter length of side c: '))

# Function call & making decision
if is_valid_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)
else:
    print('Tringle is not possible from given sides.')





















# list1=[1,2,3,4]
# # list2=[2,4,5,6]
# # list3=[2,6,7,8]
# # result=list()
# # result.extend(i for i in list1 if i not in (list2+list3) and i not in result)
# # result.extend(i for i in list2 if i not in (list1+list3) and i not in result)
# # result.extend(i for i in list3 if i not in (list1+list2) and i not in result)
# # print(result)
# # print('*',"abcde".center(6),'*',sep='')


# def descending_order(num):
#     pass
#
# def descending_order(num):
#     return int("".join(sorted([num for num in str(num)], reverse=True)))
#
# print(descending_order(2345678))