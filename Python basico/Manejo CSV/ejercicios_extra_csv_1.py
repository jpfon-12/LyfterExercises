# Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea

import csv


def read_videogames_info(file_path):
    counter = 1
    try:
        print("\n*** Informacion de videjuegos ***\n")
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for videogame in reader:
                print(f"--> Videojuego {counter}")
                print(f"Nombre: {videogame["Nombre"]}\nGenero: {videogame["Genero"]}\nDesarrollador: {videogame["Desarrollador"]}\nClasificacion: {videogame["Clasificacion ESRB"]}\n")
                counter += 1
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")


def main():
    read_videogames_info('videogames_info.csv')


main()