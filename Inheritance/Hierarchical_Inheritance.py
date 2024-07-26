
class Parent:
    def func1(self):
        print("I am your Dad")

class FirstSon(Parent):
    def func2(self):
        print("I am the eldest brother")

class SecondSon(Parent):
    def func3(self):
        print("I am the youngest brother")
obj1 = FirstSon()
obj2 = SecondSon()
obj1.func1()
obj2.func2()