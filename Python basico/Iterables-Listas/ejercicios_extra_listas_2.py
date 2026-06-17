#Cree un programa que verifique si todos los elementos de una lista son positivos

my_list = [3, 6, 0, -2, 4]
negative_number = False

for i in range(0, len(my_list)):
    if my_list[i] <= 0:
        negative_number = True

if negative_number:
    print("Hay al menos un numero negativo o cero")
else:
    print("Todos los numeros son positivos")


print(f"Esta es la lista: {my_list}")


