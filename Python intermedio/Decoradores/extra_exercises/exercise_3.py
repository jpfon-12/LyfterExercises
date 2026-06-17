# Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
# A esta función se le debe combinar dos decoradores:
# @log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
# @validate_numbers: revisa que todos los argumentos sean numéricos
from datetime import datetime

class UserMath:


    def log_call(func):
        def wrapper(first_number, second_number):
            result = func(first_number, second_number)
            print(f"Func: {func.__name__} - Arguments: {first_number}, {second_number} - [{datetime.now()}] - Result: {result}")
            return result
        return wrapper
    

    def validate_numbers(func):
        def wrapper(first_number, second_number):
            if isinstance(first_number, str) or isinstance(second_number, str):
                raise ValueError(
                    "Only numbers allowed"
                )
            return func(first_number, second_number)
        return wrapper 

    
    @validate_numbers
    @log_call
    def multiply(first_number, second_number):
        result = first_number * second_number
        return result
    


user = UserMath
print(f"Result: {user.multiply(9,10)}")

