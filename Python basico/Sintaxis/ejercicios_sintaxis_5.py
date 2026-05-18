# Dada n cantidad de notas de un estudiante, calcular:
# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

grades_number = int(input("Ingrese el numero de notas que desea registrar: "))
i = 1
failing_grades_number = 0
passing_grades_number = 0
total_passing_grades = 0
total_failing_grades = 0
total_grades = 0

while i <= grades_number:
    grade = int(input(f"Ingrese la nota {i}: "))
    if grade < 70:
        failing_grades_number = failing_grades_number + 1
        total_failing_grades = total_failing_grades + grade
    if grade >= 70:
        passing_grades_number = passing_grades_number + 1
        total_passing_grades = total_passing_grades + grade
    total_grades = total_grades + grade
    i += 1

print(f"\n* El estudiando aprobo {passing_grades_number} notas con mayor a 70")
print(f"* El estudiando reprobo {failing_grades_number} notas con menor a 70")
print(f"* El promedio total de todas las notas es {total_grades / grades_number}")

if passing_grades_number > 0:
    print(f"* Promedio notas aprobadas: {total_passing_grades / passing_grades_number}")
else:
    print("* Promedio notas aprobadas: 'no hay registro de notas aprobadas'")

if failing_grades_number > 0:
    print(f"* Promedio notas reprobadas: {total_failing_grades / failing_grades_number}")
else:
    print("* Promedio notas reprobadas: 'no hay registro de notas reprobadas'")

