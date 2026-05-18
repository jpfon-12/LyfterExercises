list_of_persons = [
    {
        "name": "Jose Fonseca",
        "age": 36,
        "id": 114150676,
        "color": "green",
    },

    {
        "name": "Juan Mora",
        "age": 25,
        "id": 112060889,
        "color": "blue",
    },

    {
        "name": "Maria Arias",
        "age": 49,
        "id": 348901006,
        "color": "purple",
    },
]

for i in range(0, len(list_of_persons)):
    print(f"Nombre: {list_of_persons[i]["name"]}")
    print(f"Id: {list_of_persons[i]["id"]}")
    print(f"Edad: {list_of_persons[i]["age"]}")
    print(" *********** ")
