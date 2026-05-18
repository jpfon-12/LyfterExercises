# Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
# Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
import random

secret_number = random.randint(1,10)
print("*** Adivine el numero secreto ***")
user_number = int(input("Ingrese su numero: "))

while user_number != secret_number:
    print("Error, vuelve a intentarlo")
    user_number = int(input("Ingrese su numero: "))

print("Felicidades, acertaste el numero secreto.")
print(f"El numero secreto era {secret_number}")
