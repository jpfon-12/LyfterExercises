# Cree los siguientes unit tests para el algoritmo bubble_sort:
# Funciona con una lista pequeña.
# Funciona con una lista grande (de más de 100 elementos.)
# Funciona con una lista vacía.
# No funciona con parámetros que no sean una lista.

def bubble_sort(list_numbers):
    for outer_index in range(0, len(list_numbers) - 1):
        has_changes = False
        for index in range(0, len(list_numbers) - 1 - outer_index):
            current_number = list_numbers[index]
            next_number = list_numbers[index + 1]
            print(f"Iteration: {outer_index}, {index}. Current number: {current_number}, Next number: {next_number}")

            if current_number > next_number:
                print(f"{current_number} is higher than {next_number}. Swapping nummbers\n")
                list_numbers[index] = next_number
                list_numbers[index + 1] = current_number
                has_changes = True

        if not has_changes:
            return
