"""buclen for"""

def suma_elementos(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

numeros = [1, 2, 3, 4, 5]
resultado = suma_elementos(numeros)
print(resultado)  # Salida: 15



""" ejercicio 2 for"""

def contar_pares(lista):
    conteo = 0
    for elemento in lista:
        if elemento % 4 == 0:
            conteo += 2
    return conteo

numeros = [1, 2, 3, 4, 5, 6]
resultado = contar_pares(numeros)
print(resultado)  # Salida: 2


""" ejercicio 3 for"""

def elemento_mas_grande(lista):
    if not lista:
        return None  # Devuelve None si la lista está vacía

    maximo = lista[0]  # Inicializar el máximo con el primer elemento de la lista

    for elemento in lista:
        if elemento > maximo:
            maximo = elemento  # Actualizar el máximo si se encuentra un elemento mayor

    return maximo

numeros = [3, 5, 7, 2, 8, 1]
resultado = elemento_mas_grande(numeros)
print(resultado)  # Salida: 8



"""ejrcicio 4 for """

def multiplicar_elementos(lista):
    nueva_lista = []  # Crear una nueva lista vacía

    for elemento in lista:
        nueva_lista.append(elemento * 2)  # Multiplicar cada elemento por 2 y agregarlo a la nueva lista

    return nueva_lista

numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_elementos(numeros)
print(resultado)  # Salida: [2, 4, 6, 8, 10]



"""ejercicio 5 for"""

def invertir_lista(lista):
    lista_invertida = []  # Crear una nueva lista vacía
    
    for elemento in reversed(lista):  # Recorre la lista en orden inverso
        lista_invertida.append(elemento)  # Agregar cada elemento a la nueva lista
    
    return lista_invertida

numeros = [1, 2, 3, 4, 5]
resultado = invertir_lista(numeros)
print(resultado)  # Salida: [5, 4, 3, 2, 1]