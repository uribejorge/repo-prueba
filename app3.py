
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


def alumno_con_mejor_nota(alumnos_notas):
    # Verificar si el diccionario no está vacío
    if not alumnos_notas:
        return None  # O una cadena vacía "" si prefieres
    
    # Inicializar variables para el alumno con la mejor nota
    mejor_alumno = None
    mejor_nota = -float('inf')  # Inicializar con el valor más bajo posible

    # Recorrer el diccionario para encontrar la mejor nota
    for alumno, nota in alumnos_notas.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno

    return mejor_alumno


alumnos_notas = {
    "Juan": 85,
    "Ana": 92,
    "Pedro": 78,
    "Luisa": 95
}

# Encontrar el alumno con la mejor nota
alumno_mejor_nota = alumno_con_mejor_nota(alumnos_notas)

# Mostrar el resultado
print(f"El alumno con la nota más alta es: {alumno_mejor_nota}")




"""ejercicio 4 Diccionarios"""


def crear_diccionario():
    diccionario = {}  # Inicializar el diccionario vacío
    
    while True:
        # Solicitar al usuario que ingrese una palabra
        palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
        
        # Permitir al usuario salir del bucle
        if palabra.lower() == 'salir':
            break
        
        # Solicitar al usuario que ingrese la definición de la palabra
        definicion = input(f"Ingresa la definición de '{palabra}': ")
        
        # Agregar la palabra y su definición al diccionario
        diccionario[palabra] = definicion
    
    return diccionario

# Crear el diccionario con las entradas del usuario
diccionario_final = crear_diccionario()

# Mostrar el diccionario completo
print("\nDiccionario completo:")
for palabra, definicion in diccionario_final.items():
    print(f"{palabra}: {definicion}")


"""ejercicio 5 Diccionarios"""


def buscar_palabra(diccionario, palabra_buscar):
    # Utilizar el método get() para obtener la definición de la palabra
    definicion = diccionario.get(palabra_buscar)
    
    # Verificar si la definición existe en el diccionario
    if definicion:
        return f"La definición de '{palabra_buscar}' es: {definicion}"
    else:
        return f"La palabra '{palabra_buscar}' no se encontró en el diccionario."

# Ejemplo de uso
diccionario = {
    "Python": "Un lenguaje de programación de alto nivel.",
    "Diccionario": "Un libro que contiene una lista de palabras con sus significados."
}

# Solicitar al usuario que ingrese una palabra para buscar
palabra = input("Ingresa la palabra que deseas buscar: ")

# Buscar la palabra en el diccionario
resultado = buscar_palabra(diccionario, palabra)

# Mostrar el resultado
print(resultado)

