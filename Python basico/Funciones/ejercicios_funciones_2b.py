#Intente acceder a una variable global desde una función y cambiar su valor.

global_variable = 7

def change_global_variable_value():
    global_variable = 3


def main():
    change_global_variable_value()
    print(global_variable)


main()


#La correccion en la funcion utilizando la palabra clave global:

# def change_global_variable_value():
#     global global_variable
#     global_variable = 3