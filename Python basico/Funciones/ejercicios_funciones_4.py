#Cree una función que le dé la vuelta a un string y lo retorne.
#“Hola mundo” → “odnum aloH”

def invert_string(my_string):
    new_string = ""
    for i in range(len(my_string) - 1, -1, -1):
        new_string += my_string[i]
    return new_string


def main():
    my_string = "Hola Mundo"
    print(invert_string(my_string))


main()


