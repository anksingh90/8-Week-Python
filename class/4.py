# Class : Inheritance
# Class 1 --> make / model
# Class 2 --> electric car - battery_size

class Car:
    def __init__(self, ubrand, umodel): # declaration of variables
        self.brand = ubrand
        self.model = umodel

    def car_name(self):     # function is called as method in python/coding lang
        return f"Car {self.brand} , Model : {self.model}"

class ElectricCar(Car):
    def __init__(self, ubrand, umodel, battery_size):
        super().__init__(ubrand, umodel)
        self.battery_size = battery_size

e_car = ElectricCar('Tata', 'Tiago', '50kWh')
print(e_car.car_name())