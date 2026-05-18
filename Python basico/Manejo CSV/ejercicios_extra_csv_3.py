# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada

import csv


def read_videogames(file_path):
    videogames_list = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for videogame in reader:
                videogames_list.append(videogame)
        return videogames_list
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def count_videogames_genre(videogames_list):
    genre_counter = {}
    for i in range(0, len(videogames_list)):
        if videogames_list[i]['Genero'] in genre_counter:
            genre_counter[videogames_list[i]['Genero']] += 1
        else:
            genre_counter[videogames_list[i]['Genero']] = 1
    return genre_counter
        


def main():
    videogames_list = read_videogames('videogames_info.csv')
    genre_counter = count_videogames_genre(videogames_list)

    print("\n*** Generos encontrados ***")
    sorted_dict = dict(sorted(genre_counter.items()))
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")


main()