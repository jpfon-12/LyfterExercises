# Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
# Un caso con números positivos
# Un caso con números negativos
# Un caso con ceros

from exercise_1_extra import NumberOperations


class TestNumberOperations:


    def test_sum_numbers_sums_with_positive_numbers(self):
        ops = NumberOperations()
        #Arrange
        first_number = 10
        second_number = 5
        #Act
        result = ops.sum_numbers(first_number, second_number)
        #Assert
        assert result == 15

    def test_sum_numbers_sums_with_negative_numbers(self):
        ops = NumberOperations()
        #Arrange
        first_number = -10
        second_number = -5
        #Act
        result = ops.sum_numbers(first_number, second_number)
        #Assert
        assert result == -15

    def test_sum_numbers_sums_with_zero_numbers(self):
        ops = NumberOperations()
        #Arrange
        first_number = 0
        second_number = 0
        #Act
        result = ops.sum_numbers(first_number, second_number)
        #Assert
        assert result == 0

    #=====================================================================

    def test_get_average_with_positive_numbers(self):
        ops = NumberOperations()
        #Arrange
        numbers = [5,8,10,3,7]
        #Act
        result = ops.get_average(numbers)
        #Assert
        assert result == 6.6

    def test_get_average_with_negative_numbers(self):
        ops = NumberOperations()
        #Arrange
        numbers = [-5,-8,-10,-3,-7]
        #Act
        result = ops.get_average(numbers)
        #Assert
        assert result == -6.6

    def test_get_average_with_zero_numbers(self):
        ops = NumberOperations()
        #Arrange
        numbers = [0,0,0,0,0]
        #Act
        result = ops.get_average(numbers)
        #Assert
        assert result == 0

    # #=====================================================================

    def test_convert_celsius_to_fahrenheit_with_positive_numbers(self):
        ops = NumberOperations()
        #Arrange
        celsius = 35
        #Act
        result = ops.convert_celsius_to_fahrenheit(celsius)       
        #Assert
        assert result == 95

    def test_convert_celsius_to_fahrenheit_with_negative_numbers(self):
        ops = NumberOperations()
        #Arrange
        celsius = -20
        #Act
        result = ops.convert_celsius_to_fahrenheit(celsius)
        #Assert
        assert result == -4

    def test_convert_celsius_to_fahrenheit_with_zero_numbers(self):
        ops = NumberOperations()
        #Arrange
        celsius = 0
        #Act
        result = ops.convert_celsius_to_fahrenheit(celsius)
        #Assert
        assert result == 32