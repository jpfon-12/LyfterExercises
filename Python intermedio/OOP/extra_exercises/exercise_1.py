# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("Please enter positive numbers.")
        area = self.width * self.height
        return area 
            

    def get_perimeter(self):
        if self.width < 0 or self.height <0:
            raise ValueError("Please enter positive numbers.")
        perimeter = (2*self.width) + (2*self.height)
        return perimeter

try:
    width = int(input("Enter the width: "))
    height = int(input(("Enter the height: ")))
    rectangle = Rectangle(width,height)
    print(f"Area: {rectangle.get_area()}")
    print(f"Perimenter: {rectangle.get_perimeter()}")
except ValueError as ex:
    print(f"\nError: {ex} ")