class Car:
    def __init__(self,mod,col,com,s_l):
       self.model=mod
       self.color=col
       self.company=com
       self.speed_limit=s_l
       print("Model is ",self.model)
       print("Color is ", self.color)
       print("Company is ", self.company)
       print("Speed limit is ", self.speed_limit)
    #---------user
    def start(self):
        print(self.model," started")
    def accelerate(self):
        print("Apply accelerate")
    def change_gear(self):
        print(self.speed_limit," Change gear drive carefully")
    def stop(self):
        self.change_gear()
        print("Car stoped")

print("----------------------------------- Ertiga Info")
c1 = Car("Ertiga","Red","Suzuki","60 km/hrs")
c1.start()
c1.accelerate()

c1.stop()
print("----------------------------------- Audi Info")
c2 = Car("Audi","White","Audi","80 km/hrs")
c2.start()
c2.accelerate()

c2.stop()
