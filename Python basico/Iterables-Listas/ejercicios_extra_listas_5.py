#Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

my_list = []
new_list = []
counter = 1

while counter <= 5:
    word = input(f"Agregue la palabra {counter}: ")
    my_list.append(word)
    counter += 1

for i in range(0, len(my_list)):
        if len(my_list[i])> 4:
            new_list.append(my_list[i])  

print(f"\nLista original: {my_list}")
print(f"\nNueva lista: {new_list}")

