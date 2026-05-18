#Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

def read_file(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            # for line in lines:
            #     print(line.strip())
            #print(lines)
        return lines
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def create_string(my_list):
    my_string = ''
    for i in my_list:
        my_string += i.strip() + " "
    #print(my_string)
    return my_string


def save_string(my_string):
    with open('archivo_2_ejercicio_extra_1.txt', 'w') as file:
        file.write(my_string)
    


def main():
    list_file_content = read_file('archivo_1_ejercicio_extra_1.txt')
    my_string = create_string(list_file_content)
    save_string(my_string)


main()