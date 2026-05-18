#Cree un programa que muestre el valor más pequeño de una lista sin usar min().
#Use una variable para comparar uno a uno

my_list = [9, 4, 7, 1, 5]
min_value = my_list[0]

for i in range(0, len(my_list)):
    if my_list[i] < min_value:
        min_value = my_list[i]
        

print(f"El menor valor es {min_value}")
