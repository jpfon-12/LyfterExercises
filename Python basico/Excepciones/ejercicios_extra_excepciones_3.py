# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total
def sum_values(my_list):
    sum = 0
    for i in range(0, len(my_list)):
        try:
            print(f"{float(my_list[i])} sumado correctamente")
            sum += float(my_list[i])
        except ValueError as ex:
            print(f"Elemento invalido '{my_list[i]}'")
    print(f"\nTotal de la suma {sum}")


def main():
    my_list = [10, "manzana", 5.5, 3, "n/a"]
    sum_values(my_list)


main()