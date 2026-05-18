# Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número. El algoritmo no debe terminar hasta que el usuario adivine el numero.

import random

secret_number = random.randint(1,10)

print("Adivine el numero secreto del 1 al 10")
user_number = int(input("Ingrese un numero: "))

while user_number != secret_number:
    print("Fallaste, intentalo de nuevo")
    user_number = int(input("Ingrese un numero: "))

print(f"Felicidades, adivinaste el numero, el numero secreto era {secret_number}")
