# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
# Lea el archivo JSON de Pokémon
# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo

import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load(file)
        return reader
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def lookup_pokemon(list_pokemon, pokemon_type):
    list_pokemons_type = []
    for pokemon in list_pokemon:
        if pokemon['type'].lower() == pokemon_type:
            list_pokemons_type.append(pokemon['name'])
    return list_pokemons_type


def main():
    list_pokemons = read_json_file('pokemones.json')
    pokemon_type = input("\nIngrese el tipo de Pokemon que desea buscar(water, electric, fire, etc): ").lower()
    list_pokemons_per_type = lookup_pokemon(list_pokemons, pokemon_type)

    if list_pokemons_per_type == []:
        print("No hay coincidencias de ese tipo")
    else:
        print("\nLos Pokemons que existen de este tipo son:")
        for pokemon_type in list_pokemons_per_type:
            print(f"-{pokemon_type}")

    
main()