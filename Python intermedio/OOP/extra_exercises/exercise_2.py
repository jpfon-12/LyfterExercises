# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Makes a sound"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)      

    def speak(self):
        return "Guau"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Miau"



dog = Dog("Firulais")
print(f"Dog: {dog.name}")
print(f"Animal sound: {dog.speak()}\n")

cat = Cat("Minino")
print(f"Cat: {cat.name}")
print(f"Animal sound: {cat.speak()}")

