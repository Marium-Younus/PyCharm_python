
#-------------------------- Collection datatype python
print(" *************************************** Learning List*******************************")
flower=["Rose","Lilly","Lotus","Tulip","Sunflower","Daffodil","Cauliflower"]
print(flower)

#-------------------Operation on list collection datatype
# print("-----------------Access Item +ve index")
# print(flower[0])
# print("-----------------Access Item -ve index")
# print(flower[-1])
# print(flower[-2])
#
# print("-----------------Access Item via range")
# print(flower[1:4])
#
# print("-----------------Access Item via start of the list")
# print(flower[:3])
#
# print("----------------- Access Item via end of the list")
# print(flower[3:])
#--------------------------------------------------------------------------------------------
# print("-----------------Change Item via index")
# flower[2] = "Orchid"
# print(flower)
# print("-----------------Change Item via range")
# flower[1:4]=["Carnation","Hyacinth","Mogra"]
# print(flower)
#
# print("-----------------Change Item via single value")
# flower[1:3]=["cauliflower"]
# print(flower)
#------------------------------------------------------------------------------------
# print("-----------------Add Item via append function")
# flower.append("Daffodil")
# print(flower)
# print("-----------------Add Item via insert function")
# flower.insert(2,"Freesia")
# print(flower)
# print("-----------------Add Item via extend function")
# flower2 = ["Galdiolus","Anemone"]
# flower.extend(flower2)
# print(flower)
# print("-----------------Add Item via tuple DT")
# flower3 = ("Galdiolus","Anemone")
# flower.extend(flower3)
# print(flower)
#------------------------------------------------------------------------------------
print("-----------------Remove Item via remove function")
flower.remove("Lilly")
print(flower)
print("-----------------Remove Item via pop function")
flower.pop(3)
print(flower)
print("-----------------Remove Item via pop function")
flower.pop()
print(flower)
print("-----------------Remove Item via del keyword")
del flower[2]
print(flower)
print("-----------------Remove Item via clear function")
flower.clear()
print(flower)
print("-----------------delete whole variable via del keyword")
del flower
print("Whole list is deleted")