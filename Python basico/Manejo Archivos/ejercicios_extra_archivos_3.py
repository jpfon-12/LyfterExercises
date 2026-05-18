# Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo

def read_file(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def convert_to_uppercase(my_list):
    my_uppercase_string = ""
    for i in my_list:
        my_uppercase_string += i.upper()
    #print(my_string)
    return my_uppercase_string


def save_uppercase_string(my_uppercase_string): 
    with open('archivo_2_ejercicio_extra_3.txt', 'w') as file:
        file.write(my_uppercase_string)


def main():
    list_file_content = read_file('archivo_1_ejercicio_extra_3.txt')
    uppercase_string = convert_to_uppercase(list_file_content)
    save_uppercase_string(uppercase_string)


main()