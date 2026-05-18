#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_first_message(message_1, message_2):
    print(message_1)
    print_second_message(message_2)


def print_second_message(message_2):
    print(message_2)
    

def main():
    print_first_message("Hola", "Mundo")
    

main()