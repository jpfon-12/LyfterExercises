#Cree un programa que le pida tres números al usuario y muestre el mayor.

first_number = int(input("Ingrese el primer numero: "))
greatest_number = first_number

second_number = int(input("Ingrese el segundo numero: "))
if second_number>greatest_number:
    greatest_number = second_number

third_number = int(input("Ingrese el tercer numero: "))
if third_number>greatest_number:
    greatest_number = third_number

print(f"El numero mayor es: {greatest_number}")