#Cree una función que reciba un string y retorne cuántas vocales contiene


def count_vowels(my_string):
    vowels = "aeiouAEIOU"
    vowel_counter = 0
    for vowel in my_string:
        if vowel in vowels:
            vowel_counter += 1
    return vowel_counter


def main():
    my_string = "Hola mundo"
    counter = count_vowels(my_string)
    print(f"Numero de vocales en el string: {counter}")


main()