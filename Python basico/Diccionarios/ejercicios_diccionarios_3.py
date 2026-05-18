#Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplos:
# list_of_keys = [’access_level’, ‘age’]
# employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
# → {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

list_of_keys = ["access_level", "age"]

dictionary_employee = {
    "name": "John", 
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

#antes del borrado
for key, value in dictionary_employee.items():
    print(f"{key}: {value}")

#borrado    

for i in range(0, len(list_of_keys)):
    deleted_key = dictionary_employee.pop(list_of_keys[i])


#despues del borrado
print(" \n*** *** *** ")
for key, value in dictionary_employee.items():
    print(f"{key}: {value}")