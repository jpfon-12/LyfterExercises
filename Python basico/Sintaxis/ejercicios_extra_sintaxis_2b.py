#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
#Ejemplos:
#23, 30, 768 → Correcto (hay un 30)
#10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

first_number = int(input("Ingrese el primer numero: "))
second_number = int(input("Ingrese el segundo numero: "))
third_number = int(input("Ingrese el tercer numero: "))

if first_number + second_number + third_number == 30:
    print(f"Correcto ({first_number} + {second_number} + {third_number} = {first_number + second_number + third_number})")
elif first_number == 30 or second_number == 30 or third_number == 30:
    print("Correcto (hay un 30)")
else:       
    print("Incorrecto (no hay ningun 30, y la suma de ellos tampoco da 30)")