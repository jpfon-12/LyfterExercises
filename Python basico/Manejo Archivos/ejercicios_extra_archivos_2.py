#Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
#(Considere que las palabras están separadas por espacios y/o saltos de línea)

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # for line in lines:
            #     print(line)
        return lines
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []
    

def count_words(my_list):
    my_string = ""
    for element in my_list:
        my_string += element
    #print(my_string)
    words = my_string.split()
    #print(words)
    number_of_words = len(words)
    return number_of_words


def main():
    list_file_content = read_file('archivo_ejercicio_extra_2.txt')
    number_of_words = count_words(list_file_content)
    print(f"Este archivo contiene '{number_of_words}' palabras")


main()    