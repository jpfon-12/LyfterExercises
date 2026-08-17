# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero.


def bubble_sort(list_numbers):
    for outer_index in range(len(list_numbers) -1, 0, -1):
        has_changes = False
        for index in range(len(list_numbers) -1, 0, -1):
            current_number = list_numbers[index]
            prev_number = list_numbers[index - 1]
            print(f"Iteration: {outer_index}, {index}. Current number: {current_number}, Prev number: {prev_number}")

            if current_number < prev_number:
                print(f"{current_number} is lower than {prev_number}. Swapping nummbers\n")
                list_numbers[index] = prev_number
                list_numbers[index - 1] = current_number
                has_changes = True

        if not has_changes:
            return


my_list = [4,2,1,5,3]
bubble_sort(my_list)

print(my_list)


