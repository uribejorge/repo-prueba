
"""Ejercicio 1 Diccionarios"""

# Crear un diccionario vacío para almacenar los datos de los alumnos
alumnos_notas = {}

# Bucle while para ingresar datos de varios alumnos
while True:
    nombre = input("Ingresa el nombre del alumno (o escribe 'salir' para terminar): ")

    if nombre.lower() == 'salir':
        break

    try:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
    except ValueError:
        print("Por favor, ingresa un número válido para la nota.")
        continue

    # Agregar el nombre y la nota al diccionario
    alumnos_notas[nombre] = nota

# Mostrar el diccionario con todos los alumnos y sus notas
print("\nDiccionario de alumnos y sus notas:")
for alumno, nota in alumnos_notas.items():
    print(f"{alumno}: {nota}")




""" ejercicio 2 Diccionarios"""


def promedio_notas(diccionario):
    if not diccionario:
        return 0  # Devuelve 0 si el diccionario está vacío
    
    suma_notas = 0
    cantidad_alumnos = 0
    
    # Recorre todas las notas en el diccionario
    for nota in diccionario.values():
        suma_notas += nota
        cantidad_alumnos += 1
    
    # Calcula el promedio
    promedio = suma_notas / cantidad_alumnos
    return promedio

alumnos_notas = {
    "Ana": 8.5,
    "Luis": 9.0,
    "Carlos": 7.5,
    "Maria": 9.5
}

resultado = promedio_notas(alumnos_notas)
print(f"El promedio de las notas es: {resultado}")  # Salida: El promedio de las notas es: 8.875



"""ejercicio 3 Diccionarios"""
