# Class - Basic / Object

class Car:
    def __init__(self, ubrand, umodel): # declaration of variables
        self.brand = ubrand
        self.model = umodel

obj = Car('Suzuki','Maruti 800')    # obj of class Car
print(obj.brand)

obj1 = Car('Tata','Tiago')
print(obj1.brand)