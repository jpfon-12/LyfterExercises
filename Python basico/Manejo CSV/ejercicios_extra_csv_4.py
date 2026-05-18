# Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible

import csv

def read_videogames(file_path):
    videogames_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for videogame in reader:
                videogames_list.append(videogame)
        return videogames_list
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []
    

def get_videogames_per_developer(videogames_list, developer):
    videogames_per_developer = []
    check_if_developer = False
    for videogame in videogames_list:
        if videogame["Desarrollador"].lower() == developer.lower():
            videogames_per_developer.append(videogame)
            check_if_developer = True
    if check_if_developer == False:
            print(f"\nNo hay registros para este desarrollador: '{developer}'. -> Verifica que los datos ingresados sean correctos")
    return videogames_per_developer


def main():
    print("\n --- Consulta de videojuegos por desarrollador --- \n")
    developer = input("Ingrese el nombre del desarrollador a consultar: ")
    videogames_list = read_videogames('videogames_info.csv')
    developer_games = get_videogames_per_developer(videogames_list, developer)
    #print(videogames_list)
    print(f"\n   Videojuegos desarrollados por {developer}:   \n")
    for game in developer_games:
        print(f"- {game['Nombre']} (Clasificacion: {game['Clasificacion ESRB']}, Genero: {game['Genero']})")


main()