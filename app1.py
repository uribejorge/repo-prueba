"""While"""

alumnos_notas ={}  #Diccionario

while True:

    nombre= input("Nombre del alumno (o salir para terminar):")

    if nombre.lower() == "salir":  #salir del bucle
        break
    while True:
        try: 
            nota = float(input(f"Introduce la nota de {nombre}:"))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe de estar entre 0 y 10. Intente de nuevo")
        except ValueError:
                print("Ingrese numero valido ")
    
    alumnos_notas[nombre] = nota

print("\n Diccionario de alumnos y notas")
for alumno, nota in alumnos_notas.items():
    print(f"{alumno}: {nota}")


    """while contador de vocales """

    #Contar vocales en una frase


frase = input("Introduce una frase: ") # ingrese una frase
vocales = "aeiou"    # Se definir las vocales
contador_vocales = 0     # Inicializar el contador de vocales
indice = 0   # Inicializar el índice para el bucle while

while indice < len(frase): # Recorre la frase con un bucle while
    caracter = frase[indice]   # Obtener el carácter actual
    
    if caracter in vocales:  # Verificar si el carácter actual es una vocal
        contador_vocales += 1
    
    # Pasar al siguiente carácter
    indice += 1

print(f"La cantidad de vocales en la frase es: {contador_vocales}") # Mostrar el número total de vocales encontradas