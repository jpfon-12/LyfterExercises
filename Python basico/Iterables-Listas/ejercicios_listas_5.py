#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#Ejemplos:
#86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

counter = 1
user_numbers = []
higher_number = 0
print("*** Ingrese 10 numeros ***")

while counter <= 10:
    number = int(input(f"Ingrese el numero {counter}: "))
    user_numbers.append(number)
    counter += 1

for i in range(0, len(user_numbers)):
    if user_numbers[i] > higher_number:
        higher_number = user_numbers[i]

print(f"\nLos numeros que ingresaste son: {user_numbers}")
print(f"El mas alto fue: {higher_number}")

