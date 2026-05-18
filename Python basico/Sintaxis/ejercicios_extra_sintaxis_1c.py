#Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
# 5 → 15 (1 + 2 + 3 + 4 + 5)
# 3 → 6 (1 + 2 + 3)
# 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

number = int(input("Ingrese un numero: "))

i = 1
total_sum = 0

while i <= number:
    total_sum = total_sum + i
    i += 1

print(f"La suma es {total_sum}")