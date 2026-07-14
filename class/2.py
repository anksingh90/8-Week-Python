# Class method
# Add a method of the Class Car that displays the full name of the car (brand & model)
# Store details - Brand, Model, Time_Of_Entry into DB. ICE - Petrol/Desiel

class Car:
    def __init__(self, ubrand, umodel): # declaration of variables
        self.brand = ubrand
        self.model = umodel

    def car_name(self):     # function is called as method in python/coding lang
        return f"Car {self.brand} , Model : {self.model}"

obj = Car('Suzuki','Maruti 800')    # obj of class Car
print(obj.car_name())

obj1 = Car('Tata','Tiago')
print(obj.car_name())
