# implementing ABC in python

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        """Child classes must implement this method"""
        pass
    
    def sleep(self):
        """A normal method with default behavior"""
        print("Zzz... animal is sleeping.")

# 2. Create a valid child class
class Dog(Animal):
    pass
    #def make_sound(self):
     #   return "Woof!"

# main()
dog = Dog()
print(dog.make_sound())  # Output: Woof!
dog.sleep()              # Output: Zzz... animal is sleeping.
