"""4.	Escribir un algoritmo que lea las cuatro notas (de 1 a 5) de un estudiante y
 permita clasificar su rendimiento de acuerdo con el promedio de la siguiente forma:

Entre 4 y 5: excelente

Ente 3 y 3.99: Bien

Entre 0 y 2,99: Deficiente
"""

# Leer las cuatro notas del estudiante
nota1 = float(input("Ingrese la primera nota (de 1 a 5): "))
nota2 = float(input("Ingrese la segunda nota (de 1 a 5): "))
nota3 = float(input("Ingrese la tercera nota (de 1 a 5): "))
nota4 = float(input("Ingrese la cuarta nota (de 1 a 5): "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Clasificar el rendimiento según el promedio
if 4 <= promedio <= 5:
    rendimiento = "Excelente"
elif 3 <= promedio < 4:
    rendimiento = "Bien"
elif 0 <= promedio < 3:
    rendimiento = "Deficiente"
else:
    rendimiento = "Las notas deben estar en el rango de 1 a 5"

# Mostrar el resultado
print(f"El promedio de notas es: {promedio:.2f}")
print(f"Rendimiento: {rendimiento}")