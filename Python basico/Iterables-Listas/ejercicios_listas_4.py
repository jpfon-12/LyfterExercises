#Cree un programa que elimine todos los números impares de una lista.
#Ejemplos:
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []

for i in range(0, len(original_list)):
    if original_list[i] % 2 == 0:
        even_list.append(original_list[i])

print(even_list)



