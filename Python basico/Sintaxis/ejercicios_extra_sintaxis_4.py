#Tabla de multiplicar personalizada
#Pida al usuario un número del 1 al 10
#Muestre su tabla de multiplicar del 1 al 12

number = int(input("Ingrese un numero del 1 al 10: "))

i = 1

while number > 10 or number < 1:
    print("Error, solo numeros del 1 al 10. Intente de nuevo.")
    number = int(input("Ingrese un numero del 1 al 10: "))

print(f"Tabla de multiplicar del {number} (1 al 12)")
while i <= 12:
    print(f"{number} x {i} = {number * i}")
    i += 1