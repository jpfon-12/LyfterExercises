# Analice el algoritmo de bubble_sort usando la Big O Notation.


def bubble_sort(list_numbers):
    for outer_index in range(0, len(list_numbers) - 1):                                                                   #n
        has_changes = False                                                                                               #n
        for index in range(0, len(list_numbers) - 1 - outer_index):                                                       #n^2
            current_number = list_numbers[index]                                                                          #n^2
            next_number = list_numbers[index + 1]                                                                         #n^2
            print(f"Iteration: {outer_index}, {index}. Current number: {current_number}, Next number: {next_number}")     #n^2

            if current_number > next_number:                                                                              #n^2
                print(f"{current_number} is higher than {next_number}. Swapping numbers\n")                               #n^2
                list_numbers[index] = next_number                                                                         #n^2      
                list_numbers[index + 1] = current_number                                                                  #n^2
                has_changes = True                                                                                        #n^2

        if not has_changes:                                                                                               #n
            return                                                                                                        #n


my_list = [1, 2, 18, 3, 4, 15, 5]                                                                                         #1
bubble_sort(my_list)                                                                                                      #1
print(my_list)                                                                                                            #1


#Big O = 9n^2 + 4n + 1 + 1 + 1 
#Big O = O(n^2)