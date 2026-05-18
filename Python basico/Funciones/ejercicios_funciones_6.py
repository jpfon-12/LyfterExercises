#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.

def sort_words(my_string):
    my_list = my_string.split("-")
    
    sorted_string = "-".join(sorted(my_list))
    return sorted_string    


def main():
    my_string = "python-variable-funcion-computadora-monitor"
    print(sort_words(my_string))


main()
