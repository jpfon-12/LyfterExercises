#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
import os
import time

def add_numbers(current_number, number):
    result = current_number + number
    return result

def subtract_numbers(current_number, number):
    result = current_number - number
    return result


def multiply_numbers(current_number, number):
    result = current_number * number
    return result


def divide_numbers(current_number, number):
    try:
        result = current_number / number
        return result
    except ZeroDivisionError as error:
        print(f"Error: Division entre cero. Detalles: {error}")
        return None
        

def get_number(): 
    while True:   
        try:
            number = int(input("Digite un numero: "))
            return number
        except ValueError as error:
            print(f"\nError: Ingresaste un string, intenta de nuevo ... Detalles: {error}")


def clear_result(): 
    number = 0
    print("Borrando resultado ...")
    time.sleep(1)
    return number


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Borrar resultado")
    print("6. Salir")


def main():
    current_number = 0
    while True:
        print("\n    *** *** C A L C U L A D O R A *** ***    \n")
        print(f"\nNumero actual: {current_number}\n")
        show_menu()
        try:
            option = int(input("\nDigite el numero de la operacion a ejecutar: "))
            clear_console()
            match option:
                case 1:
                    print(f"\nLa suma sera {current_number} + el numero que ingreses a continuacion")
                    number = get_number()
                    print(f"\n{current_number} + {number}")
                    current_number = add_numbers(current_number, number)
                    print(f"Resultado: {current_number}")
                case 2:
                    print(f"\nLa resta sera {current_number} - el numero que ingreses a continuacion")
                    number = get_number()
                    print(f"\n{current_number} - {number}")
                    current_number = subtract_numbers(current_number, number)
                    print(f"Resultado: {current_number}")
                case 3:
                    print(f"\nLa multiplicacion sera {current_number} X el numero que ingreses a continuacion")
                    number = get_number()
                    print(f"\n{current_number} X {number}")
                    current_number = multiply_numbers(current_number, number)
                    print(f"Resultado: {current_number}")
                case 4:
                    print(f"\nLa division sera {current_number} / el numero que ingreses a continuacion")
                    number = get_number()
                    print(f"\n{current_number} / {number}")
                    result = divide_numbers(current_number, number)
                    if result is not None:
                        current_number = result
                    print(f"Resultado: {current_number}")
                case 5:
                    current_number = clear_result()
                    clear_console()
                case 6:
                    break
                case _:
                    clear_console()
                    print("\nNumero invalido. Por favor ingrese un numero valido del 1 al 6")
            input("\nPresione Enter para continuar ...")
            clear_console()
        except ValueError as error:
            clear_console()
            print(f"\nError: Ingresaste un string, intenta de nuevo ... Detalles: {error}")


main()