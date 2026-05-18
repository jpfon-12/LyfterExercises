# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load(file)
        return reader
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def get_statistics(list_pokemons):
    pokemons_stats = {}
    for statistics in list_pokemons:
        pokemons_stats[statistics['name']] = {
            'PS (Puntos Salud)': statistics['stats']['hp'],
            'Ataque': statistics['stats']['attack'],
            'Defensa': statistics['stats']['defense'],
            'Ataque especial': statistics['stats']['sp_attack'],
            'Defensa especial': statistics['stats']['sp_defense'],
            'Velocidad': statistics['stats']['speed']
        }
    return pokemons_stats


def main():
    list_pokemons = read_json_file('pokemones.json')
    statistics = get_statistics(list_pokemons)
    print("\n --- Estadisticas ---\n")

    for name, stats in statistics.items():
        print(name)
        for key, value in stats.items():
            print(f"\t-{key}: {value}")


main()