#La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
#[4, 6, 2, 29] → 41

def sum_list_numbers(list_numbers):
    total_sum = 0
    for number in list_numbers:
        total_sum += number
    return total_sum


def main():
    list_numbers = [4, 6, 2, 29]
    print(sum_list_numbers(list_numbers))
   

main()
