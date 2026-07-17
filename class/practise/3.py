
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"

# main()
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Betsy")
ani = Animal("Betsy")

print(dog.speak())
print(cat.speak())
print(cow.speak())
print(ani.speak())