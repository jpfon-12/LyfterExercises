# Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente

def request_info():
    my_string = input("Ingrese una linea de texto: ")
    return my_string


def save_to_file(my_string):
    with open('archivo_1_ejercicio_extra_4.txt', 'a') as file:
            file.write(my_string + " ")
    

def main():
    my_string = request_info()
    save_to_file(my_string)
    #print(my_string)


main()