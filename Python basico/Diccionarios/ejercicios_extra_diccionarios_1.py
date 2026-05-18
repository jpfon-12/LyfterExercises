#Dada una lista de ventas con la siguiente información:
# date
# customer_email
# items
# Y cada item teniendo la siguiente información:
# name
# upc
# unit_price
# Cree un diccionario que guarde el total de ventas de cada UPC.

total_sales = {}
total_unit_price = 0
sales = [
    {
        "date": "27/02/23",
        "customer_email": "joe@gmail.com",
        "items" : [
            {
                "name": "Lava Lamp",
                "upc" : "ITEM-453",
                "unit_price": 65.76,
            },
            {                                               
                "name": "Iron",
                "upc" : "ITEM-324",
                "unit_price": 32.45,
            },
            {
                "name": "Basketball",
                "upc": "ITEM-432",
                "unit_price": 12.54,
            }
        ]
    }, 
    {
        "date": "27/02/23",
        "customer_email": "davi@gmail.com",
        "items" : [
            {
                "name": "Lava Lamp",
                "upc" : "ITEM-453",
                "unit_price": 65.76,
            },
            {
                "name": "Key Holder",
                "upc" : "ITEM-23",
                "unit_price": 5.42,
            }
        ]
    },
    {
        "date": "26/02/23",
        "customer_email": "amanda@gmail.com",
        "items" : [
            {
                "name": "Key Holder",
                "upc" : "ITEM-23",
                "unit_price": 3.42,
            },
            {
                "name": "Basketball",
                "upc" : "ITEM-432",
                "unit_price": 17.54,
            }
        ]
    }
]


for i in range(0, len(sales)):
    for j in range(0, len(sales[i]["items"])):

        if sales[i]["items"][j]["upc"] in total_sales:
            total_sales[sales[i]["items"][j]["upc"]] += sales[i]["items"][j]["unit_price"]
        else:
            total_sales[sales[i]["items"][j]["upc"]] = sales[i]["items"][j]["unit_price"]
        


for key, value in total_sales.items():
    print(f"{key}: {value}")        

 