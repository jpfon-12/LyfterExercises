# Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales

#version 1
def manual_add(number):
    result = 0                          #1
    for i in range(1, number + 1):      #n
        result += i                     #n
    return result                       #1


#version 2
def add_formula(number):
    return number * (number + 1) // 2 #1

print(manual_add(1000000000))
print(add_formula(1000000000))

# =========================================================
# Preguntas:

#1. ¿Cuál es la complejidad de cada versión?

#para version 1 la complejidad es O(n)
#para la version 2 la comlejidad es O(1)


#2. ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?

# Utilizaría la versión 2 porque su complejidad es O(1) (tiempo constante),
# mientras que la versión 1 es O(n) (tiempo lineal)


