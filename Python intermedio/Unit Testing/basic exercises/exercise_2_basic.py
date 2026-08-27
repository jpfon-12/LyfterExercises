# Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones (exceptuando el 1 y 2)


#Cree una función que le dé la vuelta a un string y lo retorne.
#“Hola mundo” → “odnum aloH”
def invert_string(my_string):
    new_string = ""
    for i in range(len(my_string) - 1, -1, -1):
        new_string += my_string[i]
    return new_string

#============================================================================================

#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
def calculate_letters(my_string):
    upper_case_count = 0
    lower_case_count = 0
    for i in range(0, len(my_string)):
        if my_string[i].isupper():
            upper_case_count += 1
        elif my_string[i].islower():
            lower_case_count += 1
    return upper_case_count, lower_case_count


#============================================================================================

#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
def get_primes(my_list):
    primes_list = []
    for i in range(0, len(my_list)):
        result = is_prime(my_list[i])
        if result:
            primes_list.append(my_list[i])
    return primes_list


def is_prime(number):
    prime_number = True
    if number <= 1:
        prime_number = False
    else:
        for i in range(2, number):
            if number % i == 0:
                prime_number = False
    return prime_number