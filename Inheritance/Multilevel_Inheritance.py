#----------------------------------------------=========== Multilevel Example 1 ===============--------------
class Animal:
    def eat(self):
        print('Eating...')
class Cat(Animal):
    def sound(self):
        print('Meow Meow Meow...')
class Kitten(Cat):
    def weep(self):
        print('Weeping...')


objkit =Kitten()
objkit.eat()
objkit.sound()
objkit.weep()

#----------------------------------------------=========== Multilevel Example 2 ===============--------------
class student: # Define a class as 'student'
    # Method
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

# Define a class as 'test' and inherit base class 'student'
class test(student):
    # Method
    def getMarks(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))
# Define a class as 'marks' and inherit derived class 'test'
class marks(test):
    # Method
    def display(self):
        print("\n\nName: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Study in: ",self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)
#----------------
m1 = marks()
m1.getStudent()     # Call base class method 'getStudent()'
m1.getMarks()       # Call first derived class method 'getMarks()'
m1.display()        # Call second derived class method 'display()'