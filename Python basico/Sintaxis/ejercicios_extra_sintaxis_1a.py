#Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:
#120 → 108
#40 → 39.2

price = int(input("Ingrese el precio del producto: "))

if price >= 100:
    discount = price * 0.10
else:
    discount = price * 0.02

print(f"El descuento es de {discount}")
print(f"Precio con descuento es de {price - discount}")
