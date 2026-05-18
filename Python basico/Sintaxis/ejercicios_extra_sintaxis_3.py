# # Convertidor de unidades de temperatura
# Pida al usuario ingresar una temperatura en Celsius
# Conviértala a Fahrenheit y Kelvin
# Muestre los tres valores
# Ejemplo:
#   Entrada:
#       "Ingrese temperatura en Celsius:" 25
#   Salida:
#       Fahrenheit: 77.0
#       Kelvin: 298.15

celsius = int(input("Ingrese la temperatura en Celsius: "))

fahrenheit = (celsius*9/5)+32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")