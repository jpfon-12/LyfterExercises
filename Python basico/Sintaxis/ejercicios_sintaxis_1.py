#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

#1. string + string
print("Hello "+" World") #---> result: Hello  World

#2. string + int 
print("Hello" + 1)  #---> TypeError: can only concatenate str (not "int") to str 

#To fix it we have to convert the int into a string
#print("Hello "+" 1") #--->result: Hello  1

#3. int + string
print(2 + "Hello") #--->TypeError: unsupported operand type(s) for +: 'int' and 'str'

#To fix it we have to convert the int into a string
#print("2 " + "Hello") #---> result: 2 Hello

#4. list + list
first_list = [1,2,3]
second_list = [4,5,6]

print(first_list + second_list)  #---> result: [1, 2, 3, 4, 5, 6]

#5. string + list

print("Hello World" + first_list) #---> TypeError: can only concatenate str (not "list") to str

#To fix it we have to convert the list of integers into a string. Investigating I found the join method to do so along with a for to traverse the list, take out each element and save it in a new variable
# string_result_list = ",".join([str(i) for i in first_list])
# print("Hello World "+string_result_list) # ---> result: Hello World 1,2,3

#6. float + int
print(1.5 + 1) #---> result 2.5

#7. bool + bool
print(False + True) #---> result: 1
print(False + False) #---> result: 0
print(True + True) #---> result: 2