#Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# number_of_stars
# rooms
# El value del key de rooms debe ser una lista, y cada habitación debe tener la siguiente información:
# number
# floor
# price_per_night


dictionary_hotel = {
    "name": "San Jose Hotel",
    "number_of_stars": 5,
    "rooms": [{
        "number": 201,
        "floor": 2,
        "price_per_night": 65,
    },
     {
        "number": 301,
        "floor": 3,
        "price_per_night": 80,
    },
     {
        "number": 401,
        "floor": 4,
        "price_per_night": 100,
    } ],
    
}

print(f"\nNombre hotel: {dictionary_hotel.get("name")}")
print(f"\nEstrellas: {dictionary_hotel.get("number_of_stars")}")
print("\nHabitaciones: ")
for room in dictionary_hotel["rooms"]:
    print(f"Numero: {room["number"]}")
    print(f"Piso: {room["floor"]}")
    print(f"Precio por noche: {room["price_per_night"]}")
    print(" ********* ")



