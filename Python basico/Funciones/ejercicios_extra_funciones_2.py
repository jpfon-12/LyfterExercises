#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras



def separate_words(my_list, number_letters):
    new_list = []
    for i in range(0, len(my_list)):
        if len(my_list[i]) > number_letters:
            new_list.append(my_list[i])
    return new_list


def main():
    my_list = ["cielo", "sol", "maravilloso", "dia"]
    number_letters = int(input("Ingrese el numero de letras minimas en la palabra: "))
    result = separate_words(my_list, number_letters)
    print(result)


main()
