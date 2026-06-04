# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).


class Bus:

    passengers = []
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers

    
    def add_passenger(self, person):
        if len(self.passengers) >= self.max_passengers:
            print(f"The bus is full")
            return
            
        self.passengers.append(person)


class Person:

    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return self.name



person1 = Person("Juan")
person2 = Person("Maria")
person3 = Person("Miguel")
person4 = Person("Ana")

bus = Bus(3)
bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.add_passenger(person4)


print(bus.passengers)


