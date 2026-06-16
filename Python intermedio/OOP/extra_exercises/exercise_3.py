# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity


class Inventory:

    def __init__(self):
        self.list_products = []


    def add_product(self, product):
        self.list_products.append(product)


    def show_products(self):
        for product in self.list_products:
            print(f"\nProduct: {product.product_name}")
            print(f"Price: {product.price}")
            print(f"Quantity: {product.quantity}")


    def calculate_total_value_inventory(self):
        self.total_value_inventory = 0
        for product in self.list_products:
            self.total_value_inventory += (product.quantity * product.price)
        return self.total_value_inventory


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

inventory.show_products()
print(f"\nTotal value of inventory: {inventory.calculate_total_value_inventory()}")


