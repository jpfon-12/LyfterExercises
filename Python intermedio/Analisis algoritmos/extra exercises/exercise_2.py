# Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:            #n
        if item == target:          #n
            return True             #n
    return False                    #1

# =========================================

def binary_search(my_list, target):
    low = 0                         #1
    high = len(my_list) - 1         #1
    while low <= high:              #log n (el ciclo disminuye la cantidad de iteraciones)
        mid = (low + high) // 2     #log n
        if my_list[mid] == target:  #log n
            return True             #log n
        elif my_list[mid] < target: #log n
            low = mid + 1           #log n
        else:
            high = mid - 1          #log n
    return False                    #1

# ============================================

# Preguntas:

#1. ¿Cuál es la complejidad de cada algoritmo?

#algoritmo 1 = complejidad es O(n)
#algoritmo 2 = complejidad es O(log n)

#2. ¿En qué condiciones conviene usar cada uno?

#El algoritmo 1 conviene usarlo cuando la lista esta desordenada porque el linear search va a revisar cada elemento
#independientemente del tamano de la lista
#El algoritmo 2 conviene usarlo cuando la lista esta ordenada de manera que la busqueda sea mas facil y el resultado esperado

#3. ¿Qué pasa si la lista no está ordenada?
#Si la lista no esta ordenada el algoritmo 1 siempre va a iterar cada elemento debido a que es lineal, mientras que
#el algoritmo 2 nos puede dar un resultado inexacto debido a que descartara elementos al procesar la busqueda