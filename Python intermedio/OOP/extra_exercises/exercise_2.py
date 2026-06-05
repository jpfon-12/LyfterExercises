# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self, animal_sound):
        return animal_sound


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)      


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)




dog = Dog("Firulais")
print(dog.name)
print(dog.speak("Guau"))

cat = Cat("Minino")
print(cat.name)
print(cat.speak("Miau"))

