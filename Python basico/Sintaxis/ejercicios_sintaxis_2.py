#Cree un programa que le pida al usuario su nombre, apellido, y age, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su age: "))

if age >= 0 and age <=2:
    print("Eres bebe")
elif age >=3 and age <=9:
    print("Eres niño")
elif age >=10 and age <=12:
    print("Eres preadolescente")
elif age >=13 and age <=18:
    print("Eres adolescente")
elif age >=19 and age <=25:
    print("Eres adulto joven")
elif age >=26 and age <=59:
    print("Eres adulto")
else: 
    print("Eres adulto mayor")