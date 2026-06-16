# Cree un decorador que haga print de los parámetros y retorno de la función que decore.


class BMI:

    def positive_numbers_only(func):
        def wrapper(weight, height):
            if weight < 0 or height < 0:
                raise ValueError(
                    "Error. Please enter positive numbers"
                )
            print(f"The parameters of the function are weight: {weight} and height: {height}")
            return func(weight, height)
        return wrapper


    @positive_numbers_only
    def calculate_bmi(weight, height):
        bmi = weight / (height **2)
        return bmi


bmi = BMI
print(f"BMI = {bmi.calculate_bmi(85, 1.75)}")


