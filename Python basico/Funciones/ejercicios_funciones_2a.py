#Experimente con el concepto de scope:
# 1 - Intente acceder a una variable definida dentro de una función desde afuera.



def contain_local_variable():
    number = 7


def main():
    print(number)
    
    
main()

#En este caso, la ejecucion arroja el siguiente error: "NameError: name 'number' is not defined"
#Debido a que la variable dentro de la funcion solo vive y muere dentro de ella, se puede corregir devolviendo el valor de la variable con un return dentro de la funcion para poder acceder a esa variable desde afuer:


# def contain_local_variable():
#     number = 7
#     return number

# def main():
#     local_variable_value = contain_local_variable()
#     print(local_variable_value)

# main()