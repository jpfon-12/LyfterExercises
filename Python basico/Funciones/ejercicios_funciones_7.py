#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.


def get_primes(my_list):
    primes_list = []
    for i in range(0, len(my_list)):
        result = is_prime(my_list[i])
        if result:
            primes_list.append(my_list[i])
    return primes_list
    #print(f"\nLa lista de numeros primos es {primes_list}")


def is_prime(number):
    prime_number = True
    #print(f"\nEl numero recibido en la funcion 'is_prime' es {number}")
    if number <= 1:
        prime_number = False
    else:
        for i in range(2, number):
            if number % i == 0:
                #print(f"{number} % {i} = {number%i}")
                prime_number = False
    return prime_number

def main():
    my_list = [1, 4, 6, 7, 13, 9, 67, 2]
    print(f"\nLista original es {my_list}")
    print(f"\nLa lista de numeros primos es {get_primes(my_list)}")
    
main()

