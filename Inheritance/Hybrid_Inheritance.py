
class PC:
    def func1(self):
        print("This is PC class")

class Laptop(PC):
    def func2(self):
        print("This is Laptop class inheriting PC class")

class Mouse(Laptop):
    def func3(self):
        print("This is Mouse class inheriting Laptop class")

class Student(Mouse,Laptop):
    def func4(self):
        print("This is Student class inheriting Mouse and Laptop")

#Driver's Code
objstd = Student()
objmouse = Mouse()

objstd.func4()
objmouse.func3()