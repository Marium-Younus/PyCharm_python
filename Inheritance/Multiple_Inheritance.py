
class Father:
    def func1(self):
          print("I am your dad!")

class Mother:
    def func2(self):
         print("I am your mom!")

class Child(Father, Mother):
    def func3(self):
         print("Hi mom and dad")

ob = Child()
ob.func1()
ob.func2()
ob.func3()