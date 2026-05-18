# Agrupar empleados por departamento
# Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:

department_employees = {}
employees = [
    {
        "name": "Carlos",
        "email": "carlos@empresa.com",
        "department": "Ventas"
    },
    {
        "name": "Ana",
        "email": "ana@empresa.com",
        "department": "TI"
    },
    {
        "name": "Luis",
        "email": "luis@empresa.com",
        "department": "Ventas"
    },
    {
        "name": "Sofia",
        "email": "sofia@empresa.com",
        "department": "RRHH"
    }
]

for i in range(0, len(employees)):
    if employees[i]["department"] in department_employees:
        department_employees[employees[i]["department"]].append(employees[i]["name"])
    else:
        department_employees[employees[i]["department"]] = [employees[i]["name"]]

for key, value in department_employees.items():    
    print(f"Empleados departamento de {key}: {value}")