from exercise_2_basic import invert_string, calculate_letters, get_primes


def test_invert_string_inverts_all_strings_correctly():
    #Arrange
    my_string = "Hello world"
    #Act
    result = invert_string(my_string)
    #Assert
    assert result == "dlrow olleH"


def test_invert_string_inverts_with_empty_string():
    #Arrange
    my_string = " "
    #Act
    result = invert_string(my_string)
    #Assert
    assert result == " "


def test_invert_string_inverts_all_strings_with_one_character():
    #Arrange
    my_string = "H"
    #Act
    result = invert_string(my_string)
    #Assert
    assert result == "H"


#===========================================================================================



def test_calculate_letters_calculates_number_of_upper_and_lower_letters_in_string():
    #Arrange
    my_string = "I love Nacion sushi"
    #Act
    upper_count, lower_count = calculate_letters(my_string)
    #Assert
    assert upper_count == 2
    assert lower_count == 14


def test_calculate_letters_calculates_number_of_upper_and_lower_letters_in_empty_string():
    #Arrange
    my_string = " "
    #Act
    upper_count, lower_count = calculate_letters(my_string)
    #Assert
    assert upper_count == 0
    assert lower_count == 0


def test_calculate_letters_calculates_number_of_upper_and_lower_letters_in_one_character_string():
    #Arrange
    my_string = "I"
    #Act
    upper_count, lower_count = calculate_letters(my_string)
    #Assert
    assert upper_count == 1
    assert lower_count == 0


#==========================================================================================

def test_get_primes_returns_the_prime_numbers_of_a_list():
    #Arrange
    my_list = [1, 4, 6, 7, 13, 9, 67, 2]
    #Act
    result = get_primes(my_list)
    #Assert
    assert result == [7, 13, 67, 2]


def test_get_primes_returns_the_prime_numbers_of_an_empty_list():
    #Arrange
    my_list = []
    #Act
    result = get_primes(my_list)
    #Assert
    assert result == []


def test_get_primes_returns_the_prime_numbers_of_a_list_with_negative_numbers_and_zero():
    #Arrange
    my_list = [-7, -2, 0, 1, 2, 3]
    #Act
    result = get_primes(my_list)
    #Assert
    assert result == [2, 3]