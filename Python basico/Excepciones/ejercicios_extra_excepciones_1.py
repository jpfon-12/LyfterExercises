#Cree un programa que:
# Pida al usuario su nombre
# Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número"). Luego pida su edad
# Si no es un número válido, capture el ValueError y muestre un mensaje
# Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

def ask_user_name():
    name = input("Ingrese su nombre: ")
    return name
            

def ask_user_age(): 
    age = input("Ingrese su edad: ")
    return age
    

def validate_name(name):
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero")


def validate_age(age):
    if not age.isdigit():
        raise ValueError("Numero no valido")  


def main():
     try:
        name = ask_user_name()
        validate_name(name)
        age = ask_user_age()
        validate_age(age)
        print(f"Hola {name}, su edad es {age}")
     except ValueError as ex:
        print(ex)


main()