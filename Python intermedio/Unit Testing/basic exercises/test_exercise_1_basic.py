# Cree los siguientes unit tests para el algoritmo bubble_sort:

import pytest 
import random
from exercise_1_basic import bubble_sort

# Funciona con una lista pequeña.
def test_bubble_sort_works_with_small_list():
    #Arrange
    my_list = [8,2,9,0,5]
    #Act
    bubble_sort(my_list)
    #Assert
    assert my_list == [0,2,5,8,9]


# Funciona con una lista grande (de más de 100 elementos.)
def test_bubble_sort_works_with_big_list():
    #Arrange
    my_list = random.sample(range(0, 150), 101)
    sorted_numbers = sorted(my_list)
    #Act
    bubble_sort(my_list)
    #Assert
    assert my_list == sorted_numbers


# Funciona con una lista vacía.
def test_bubble_sort_works_with_empty_list():
    #Arrange
    my_list = []
    #Act
    bubble_sort(my_list)
    #Assert
    assert my_list == []


# No funciona con parámetros que no sean una lista.
def test_bubble_sort_fails_with_no_list():
    #Arrange
    my_list = True
    #Act/Assert
    with pytest.raises(TypeError):
        bubble_sort(my_list)
    