# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:

import json


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load(file)
        return reader
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []
    

def get_type_and_level(list_pokemons):
    type_and_level_pokemons = {}
    for pokemon in list_pokemons:
        if pokemon['type'] in type_and_level_pokemons:
            type_and_level_pokemons[pokemon['type']]['sum'] += pokemon['level']
            type_and_level_pokemons[pokemon['type']]['counter'] += 1
        else:
            type_and_level_pokemons[pokemon['type']] = {
                'sum':pokemon['level'],
                'counter':1
            }
    return type_and_level_pokemons


def get_average(type_level_list):
    dict_average = {}
    for type_pokemon, data in type_level_list.items():
        average = data['sum']/data['counter']
        dict_average[type_pokemon]=average
    return dict_average


def main():
    list_pokemons = read_json_file('pokemones.json')
    type_level_pokemons = get_type_and_level(list_pokemons)
    level_average = get_average(type_level_pokemons)

    for pokemon_type, level_average in level_average.items():
        print(f"Tipo: {pokemon_type} -> Promedio de nivel: {level_average}")


main()