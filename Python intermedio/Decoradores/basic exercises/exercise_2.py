# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

class Triangle:

    def numbers_only(func):
        def wrapper(base, height):
            if isinstance(base, str) or isinstance(height, str):
                raise ValueError(
                    "Error. Only numbers allowed"
                    )
            return func(base, height)
        return wrapper
    
    @numbers_only
    def calculate_area(base, height):
        area = (base * height) / 2
        return area
    

triangle = Triangle
print(triangle.calculate_area(3,7))

