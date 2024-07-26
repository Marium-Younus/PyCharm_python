class MyCar:
    # def __int__(self):
    #     print("i am default constructor")
    def __init__(self,model,company,color,year,speed_limit):
        print("i am parameterized constructor")
        self.model=model
        self.company=company
        self.color = color
        self.year = year
        self.speed_limit = speed_limit
        print("Car model is :",self.model)
        print("Car company is :", self.company)
        print("Car color is :", self.color)
        print("Car year is :", self.year)
        print("Car speed limit is :", self.speed_limit)
    @classmethod
    def myfunct(self):
        print("user function")

