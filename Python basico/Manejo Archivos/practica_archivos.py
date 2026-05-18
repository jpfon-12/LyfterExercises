# with open('quijote.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('quijote.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

#     for number, line in enumerate(lines, start=1):
#         print(f"Line {number}: {line.strip()}")


# new_text ="Capítulo II. Que trata de la primera salida que de su tierra hizo el ingenioso Don Quijote."

# with open('quijote2.txt', 'w', encoding='utf-8') as file:
#         file.write(new_text)


extra_text ="Agregando mas al archivo."

with open('quijote2.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + extra_text)

