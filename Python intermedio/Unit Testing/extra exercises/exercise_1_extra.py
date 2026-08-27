# Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
# Un caso con números positivos
# Un caso con números negativos
# Un caso con ceros


class NumberOperations:
 
    def sum_numbers(self, a, b):
        #Add two numbers
        result = a + b
        return result
 
    def get_average(self, numbers):
        #Calculate the average of a list of numbers
        total = sum(numbers)
        amount = len(numbers)
        result = total / amount
        return result
 
    def convert_celsius_to_fahrenheit(self, celsius):
        #Convert Celsius to Fahrenheit
        result = (celsius * 9 / 5) + 32
        return result