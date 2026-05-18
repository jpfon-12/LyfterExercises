#Lea sobre el resto de métodos del módulo csv y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import csv


def save_videogames_info(file_path, data):
    with open(file_path, 'w',encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, dialect='excel-tab') #class csv.excel_tab. La clase excel_tab define las propiedades usuales de un archivo delimitado por tabulaciones generado por Excel. Esta registrada con el nombre de dialecto 'excel-tab'.
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
        save_videogames_info('videogames_info_with_tabs.csv', list_videogames)
        print("\n --- Datos guardados con exito --- ")

    except ValueError as ex:
        print(f"Error. Ingrese un numero entero. Error {ex}")


main()