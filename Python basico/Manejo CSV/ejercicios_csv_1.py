# #Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
# Nombre
# Género
# Desarrollador
# Clasificación ESRB

import csv


def save_videogames_info(file_path, data):
    with open(file_path, 'w',encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def ask_videogames_info(number_videogames):
    counter = 1
    videogames_info = []

    while counter <= number_videogames:
        print(f"\n*** Ingrese los datos del videojuego {counter} ***")
        name =input("Nombre: ")
        genre = input("Genero: ")
        developer = input("Desarrollador: ")
        rating = input("Clasificacion ESRB: ")

        videogame = {
            "Nombre": name,
            "Genero": genre,
            "Desarrollador": developer,
            "Clasificacion ESRB": rating
        }

        videogames_info.append(videogame)
        counter += 1
    return videogames_info


def main():
    try:
        number_videogames = int(input("\nCuantos videojuegos desea ingresar: "))
        list_videogames = ask_videogames_info(number_videogames)
        save_videogames_info('videogames_info.csv', list_videogames)
        print("\n --- Datos guardados con exito --- ")

    except ValueError as ex:
        print(f"Error. Ingrese un numero entero. Error {ex}")


main()