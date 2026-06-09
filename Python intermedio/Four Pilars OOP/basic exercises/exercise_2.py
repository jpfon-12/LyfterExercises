# Cree una clase abstracta de Shape que:
# Tenga los métodos abstractos de calculate_perimeter y calculate_area.
# Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
# Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass



class Circle(Shape):
    def calculate_area(self, radius):
        self.radius = radius
        area = math.pi * (self.radius ** 2)
        return area

    def calculate_perimeter(self, radius):
        self.radius = radius
        perimeter = 2 * (math.pi * self.radius)
        return perimeter



class Square(Shape):
    def calculate_area(self, side):
        self.side = side
        area = self.side ** 2
        return area

    def calculate_perimeter(self, side):
        self.side = side
        perimeter = 4 * self.side
        return perimeter



class Rectangle(Shape):
    def calculate_area(self, width, height):
        self.width = width
        self.height = height
        area  = self.width * self.height
        return area

    def calculate_perimeter(self, width, height):
        self.width = width
        self.height = height
        perimeter = 2 * (self.width * self.height)
        return perimeter




circle = Circle()
print(f"\nArea of the circle: {circle.calculate_area(3)}")
print(f"Perimeter of the circle: {circle.calculate_perimeter(3)}")
print("="*15)

square = Square()
print(f"Area of the square: {square.calculate_area(3)}")
print(f"Perimeter of the square: {square.calculate_perimeter(3)}")
print("="*15)

rectangle = Rectangle()
print(f"Area of the rectangule: {rectangle.calculate_area(3, 6)}")
print(f"Perimeter of the rectangule: {rectangle.calculate_perimeter(3, 6)}")
print("="*15)