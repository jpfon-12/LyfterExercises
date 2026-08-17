# Conteo de pasos (bubble_sort_steps)
# Modifique su implementación de bubble_sort para que:
# Cuente cuántas iteraciones (pasadas) realiza el algoritmo
# Cuente cuántos intercambios se hicieron en total


def bubble_sort_steps(list_to_sort):
    iteration = 0
    swapping = 0
    for outer_index in range(0, len(list_to_sort) - 1):
        has_changes = False
        for index in range(0, len(list_to_sort) - 1 - outer_index):
            current_number = list_to_sort[index]
            next_number = list_to_sort[index + 1]
            print(f"Iteration: {outer_index}, {index}. Current number: {current_number}, Next number: {next_number}")
            iteration += 1

            if current_number > next_number:
                print(f"--> {current_number} is higher than {next_number}. Swapping numbers\n")
                list_to_sort[index] = next_number
                list_to_sort[index + 1] = current_number
                has_changes = True
                swapping += 1
                # print(f"List so far: {list_to_sort}\n")

        if not has_changes:
            break
        
    print(f"\nIteration: {iteration}")
    print(f"Swapping: {swapping}")



my_list = [1,5,3,2,4]
bubble_sort_steps(my_list)

print(f"\nSorted list: {my_list}")