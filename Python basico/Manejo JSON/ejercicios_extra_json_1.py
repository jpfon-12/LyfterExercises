# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

import json


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load(file)
        return reader
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []
    

def show_pokemon(list_pokemons):
    print("\n---Lista de Pokemons---\n")
    for pokemon in list_pokemons:
        print(f"Nombre:  {pokemon['name']}")
        print(f"Tipo: {pokemon['type']}")
        print(f"Nivel: {pokemon['level']}")
        print(f"Peso (kg): {pokemon['weight_kg']}")
        print("Brilla: Si" if pokemon['is_shiny'] else "Brilla: No")
        print(f"Objeto que lleva: Ninguno " if pokemon['held_item'] == None else f"Objeto que lleva: {pokemon['held_item']}" )
        print(f"Habilidades:")
        for skill in pokemon['skills']:
            print(f"\t-{skill}")
        print("\n")


def main():
    list_pokemons = read_json_file('pokemones.json')
    show_pokemon(list_pokemons)


main()