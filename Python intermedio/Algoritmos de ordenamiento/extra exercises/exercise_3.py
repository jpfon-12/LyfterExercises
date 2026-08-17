# Validación de entrada antes de ordenar
# Cree una función que reciba una lista y valide:
# Que todos los elementos sean números
# Que no esté vacía
# Luego aplique bubble_sort si pasa las validaciones
# Si hay error, debe lanzar un mensaje apropiado



def validated_bubble_sort(list_to_sort):
    try:
        if list_to_sort == []:
            print("Error, the list is empty ")
            return []   
        bubble_sort(list_to_sort)
        return list_to_sort

    except TypeError as er:
        print(f"Error, the list contains letters - {er}")
        return []


def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        has_change = False
        for index in range(0, len(list_to_sort) - 1 - outer_index):
            current_number = list_to_sort[index]
            next_number = list_to_sort[index + 1]

            if current_number > next_number:
                list_to_sort[index] = next_number
                list_to_sort[index + 1] = current_number
                has_change = True

        if not has_change:
            return 


my_list = [8,1,6,10,"hi",7,5]
print(validated_bubble_sort(my_list))

