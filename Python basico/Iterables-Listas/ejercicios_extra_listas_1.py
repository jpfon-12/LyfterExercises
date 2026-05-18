#Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

my_list = []
counter_repeated_number = 0

while True:
    number = int(input("Ingrese un numero: "))
    my_list.append(number)

    answer_continue = input("Desea agregar otro numero? y/n ")
    while answer_continue != "n" and answer_continue != "y":
        print("Error, ingrese 'y' para continuar o 'n' para salir")
        answer_continue = input("Desea agregar otro numero? y/n ")

    if answer_continue == 'n':
        break 
    
lookup_number = int(input("Ingrese el numero que desea buscar: "))

for i in range(0, len(my_list)):
    if my_list[i] == lookup_number:
        counter_repeated_number = counter_repeated_number + 1


print(my_list)
print(f"El numero {lookup_number} aparece {counter_repeated_number} veces")