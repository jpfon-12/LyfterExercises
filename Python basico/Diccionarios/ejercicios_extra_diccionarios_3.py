#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.

price_categories = {}
products = [
    {
        "name": "Monitor",
        "category": "Electronica",
        "price": 200
    },
    {
        "name": "Teclado",
        "category": "Electronica",
        "price": 50
    },
    {
        "name": "Silla",
        "category": "Muebles",
        "price": 100
    },
    {
        "name": "Mesa",
        "category": "Muebles",
        "price": 280
    },
    {
        "name": "Mouse",
        "category": "Electronica",
        "price": 25
    }
]

for i in range(0, len(products)):
    if products[i]["category"] in price_categories:
        price_categories[products[i]["category"]] += products[i]["price"]
    else:
        price_categories[products[i]["category"]] = products[i]["price"]


for key, value in price_categories.items():
    print(key, value)