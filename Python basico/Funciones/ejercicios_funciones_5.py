#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

def calculate_letters(my_string):
    upper_case_count = 0
    lower_case_count = 0

    for i in range(0, len(my_string)):
        if my_string[i].isupper():
            upper_case_count += 1
        elif my_string[i].islower():
            lower_case_count += 1

    print(f"There’s {upper_case_count} upper cases and {lower_case_count} lower cases")


def main():
    my_string = "I love Nacion sushi"
    calculate_letters(my_string)

main()