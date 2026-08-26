# Analice la siguiente función:


def print_all_pairs(my_dict):
    for key1 in my_dict:                #n
        for key2 in my_dict:            #n^2
            print(f"{key1}-{key2}")     #n^2


#=========================================

#Preguntas:

#1. ¿Cuál es la complejidad temporal?
#La complejidad es n^2 

#2. ¿Cuanto dura si hay 1 millón de claves?
#Con 1 millon de claves el algoritmo debe iterar 1 000 000 X 1 000 000 = 1 billon de veces lo cual es bastante 
# considerando tambien que cada iteracion debe imprimir las llaves lo cual tiene costo de I/O y aumenta el tiempo 
# de ejecucion. La duracion puede tomar minutos, horas o dias 