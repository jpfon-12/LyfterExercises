#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

my_list = [10, 20, 30, 40, 50]
new_list = []
total = 0

for i in range(0, len(my_list)):
    total = total + my_list[i]

average = total / len(my_list)

for i in range(0, len(my_list)):
    if my_list[i] > average:
        new_list.append(my_list[i])

print(f"Promedio: {average}")
print(f"Nueva lista es: {new_list}")
