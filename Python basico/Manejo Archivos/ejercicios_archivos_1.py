#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_unsorted_songs(path):
    my_list = []
    try: 
        with open(path, 'r') as file:
            lines = file.readlines()
        for  line in lines:
            my_list.append(line.strip())
        return my_list
    except FileNotFoundError as ex:
        print(f"Error: El archivo no existe. Error: {ex}")
        return []


def sort_songs(my_list):
    return sorted(my_list)


def save_sorted_songs(sorted_list):
    with open('canciones_ordenadas.txt', 'w') as file:
        for i in range(0, len(sorted_list)):
            file.write(sorted_list[i] + "\n")


def main():
    my_list = read_unsorted_songs('canciones_desordenadas.txt')
    sorted_list = sort_songs(my_list)
    save_sorted_songs(sorted_list)


main()
