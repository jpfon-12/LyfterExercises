# Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
def convert_to_int(my_list):
    for i in range(0, len(my_list)):
        try:
            print(f"'{my_list[i]}' convertido a {int(my_list[i])}")
        except ValueError as ex:
            print(f"No se pudo convertir el elemento '{my_list[i]}'")


def main():
    my_list = ["4", "hola", "10", "5.2"]
    convert_to_int(my_list)


main()
