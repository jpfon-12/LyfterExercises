# Dada la función.
# Cree un test que:
# Valide que dividir(10, 2) retorna 5.0
# Verifique que dividir por cero lanza un ValueError
# Valide que dividir con un string como parámetro también lanza TypeError

from exercise_2_extra import divide
import pytest

def test_divide_validates_division_correctly():
    #Arrange
    first_number = 10
    second_number = 2
    #Act
    result = divide(first_number, second_number)
    #Assert
    assert result == 5


def test_divide_validates_division_by_zero():
    #Arrange
    first_number = 10
    second_number = 0
    #Act/Assert
    with pytest.raises(ValueError):
        divide(first_number, second_number)


def test_divide_validates_division_with_string():
    #Arrange
    first_number = 10
    second_number = "hello"
    #Act/Assert
    with pytest.raises(TypeError):
        divide(first_number, second_number)