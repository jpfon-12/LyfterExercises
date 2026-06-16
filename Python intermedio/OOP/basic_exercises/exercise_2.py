# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).


class Bus:
    
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    
    def get_on_passengers(self, person):
        if len(self.passengers) >= self.max_passengers:
            print(f"\nThe bus is full")
            return
        self.passengers.append(person)


    def get_off_passengers(self, person):
        self.passengers.remove(person)




class Person:

    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return self.name


bus = Bus(3) #sets the max number of passengers 

person1 = Person("Juan")
person2 = Person("Maria")
person3 = Person("Miguel")
person4 = Person("Ana")

bus.get_on_passengers(person1)
bus.get_on_passengers(person2)
bus.get_on_passengers(person3)
bus.get_on_passengers(person4)
print(f"\nPassengers on the bus: {bus.passengers}")

bus.get_off_passengers(person1)
bus.get_off_passengers(person2)
bus.get_off_passengers(person3)
print(f"\nPassengers got off the bus: {bus.passengers}")



