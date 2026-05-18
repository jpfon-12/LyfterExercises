#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto


def count_letter(text, letter):
    counter = 0
    for i in range(0, len(text)):
        if text[i] == letter:
            counter += 1
    return counter


def main():
    text = "programacion"
    letter = input("Ingrese el caracter que desea buscar: ")
    counter = count_letter(text, letter)
    print(f"El caracter {letter} aparece {counter} veces")


main()