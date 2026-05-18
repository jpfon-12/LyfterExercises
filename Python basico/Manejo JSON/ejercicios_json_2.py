# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (ipsum:lesson/python-bsico/manejo-de-json)
# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def read_json_file(path_json_file):
    try:
        with open(path_json_file, 'r', encoding='utf-8') as file:
            list_pokemons = json.load(file)
        return list_pokemons
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def add_new_pokemon(list_existing_pokemons):
    print("\n Vamos a agregar un nuevo Pokemon \n")
    try:
        name = input("Nombre del Pokémon: ")
        pokemon_type = input("Tipo (Fire, Water, Electric...): ")
        level = int(input("Nivel: "))
        weight_kg = float(input("Peso (kg): "))
        is_shiny = input("¿Es shiny? (s/n): ").lower()
        while True:
            if is_shiny == "s":
                is_shiny = True
                break
            if is_shiny == "n":
                is_shiny = False
                break
            else:
                print("Error, ingrese solo 's' para Si o 'n' para No")
                is_shiny = input("¿Es shiny? (s/n): ").lower()

        held_item = input("Objeto que lleva (Presione Enter si ninguno): ") or None

        skills = []
        print("\nIngrese las habilidades (Presione Enter para terminar)")
        while True:
            skill = input("Habilidad: ")
            if skill == "":
                break
            skills.append(skill)

        print("\n Estadisticas")
        hp = int(input("  HP: "))
        attack = int(input("  Attack: "))
        defense = int(input("  Defense: "))
        sp_attack = int(input("  Sp. Attack: "))
        sp_defense = int(input("  Sp. Defense: "))
        speed = int(input("  Speed: "))
    except ValueError as ex:
        print(f"\nError: Entrada no valida. Por favor, ingrese solo numeros enteros. Detalles: {ex}")
        return []

    new_pokemon = {
        "name":name,
        "type":pokemon_type,
        "level":level,
        "weight_kg":weight_kg,
        "is_shiny":is_shiny,
        "held_item":held_item,
        "skills": skills,
        "stats": {
            "hp":hp,
            "attack":attack,
            "defense":defense,
            "sp_attack":sp_attack,
            "sp_defense":sp_defense,
            "speed":speed
        }
    }
    list_existing_pokemons.append(new_pokemon)
    return list_existing_pokemons


def save_pokemon_json_file(path_json_file, new_pokemon):
    if new_pokemon == []:
        print("\nProblema al guardar en archivo json")
    else:
        try:
            with open(path_json_file, 'w', encoding='utf-8') as file:
                json.dump(new_pokemon, file, indent=4)
                print("Pokemon guardado con exito")
        except FileNotFoundError as ex:
            print(f"Error: El archivo no existe. Error: {ex}")
        except TypeError as ex:
            print(f"Error: Algun dato no se puede guardar en JSON file. Error: {ex}")

        


def main():
    list_existing_pokemons = read_json_file('pokemones.json')
    updated_list = add_new_pokemon(list_existing_pokemons)
    save_pokemon_json_file('pokemones.json', updated_list)


if __name__ == "__main__":
    main()