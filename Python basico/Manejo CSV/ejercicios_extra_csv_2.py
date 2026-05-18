# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

import csv


def read_videogames_rating(file_path, rating):
    check_if_rating = False
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(f"\n*** Videojuegos con clasificacion {rating} ***\n")
            for videogame in reader:
                if videogame['Clasificacion ESRB'] == rating:
                    print(f"- {videogame['Nombre']}")
                    check_if_rating = True        
            if check_if_rating == False:
                print(f"No hay registros para esta clasificacion: {rating}")
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")


def main():
    print("\n --- Consulta de videojuegos por clasificacion --- \n")
    rating = input("Ingrese la clasificacion a consultar: ").upper()
    read_videogames_rating('videogames_info.csv', rating)


main()