from exercise_2_basic import invert_string, calculate_letters, get_primes


def test_invert_string_inverts_all_strings_correctly():
    #Arrange
    my_string = "Hello world"
    #Act
    result = invert_string(my_string)
    #Assert
    assert result == "dlrow olleH"



def test_calculate_letters_calculates_number_of_upper_and_lower_letters_in_string():
    #Arrange
    my_string = "I love Nacion sushi"
    #Act
    upper_count, lower_count = calculate_letters(my_string)
    #Assert
    assert upper_count == 2
    assert lower_count == 14


def test_get_primes_returns_the_prime_numbers_of_a_list():
    #Arrange
    my_list = [1, 4, 6, 7, 13, 9, 67, 2]
    #Act
    result = get_primes(my_list)
    #Assert
    assert result == [7, 13, 67, 2]
